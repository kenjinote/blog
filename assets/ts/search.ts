interface SearchPage {
    url: string;
    excerpt: string;
    meta: { title?: string; image?: string };
}

interface SearchHit { data(): Promise<SearchPage>; }

interface SearchEngine {
    options(options: object): Promise<void>;
    search(query: string): Promise<{ results: SearchHit[] }>;
}

/** Fetch only the current language's index shards and visible result pages. */
class Search {
    private input: HTMLInputElement;
    private list: HTMLDivElement;
    private status: HTMLElement;
    private progress: HTMLElement;
    private more: HTMLButtonElement;
    private engine: Promise<SearchEngine> | undefined;
    private results: SearchHit[] = [];
    private shown = 0;
    private version = 0;
    private timer: ReturnType<typeof setTimeout> | undefined;
    private composing = false;
    private readonly pageSize = 20;

    constructor(private form: HTMLFormElement) {
        this.input = form.querySelector('input[name="keyword"]');
        this.list = document.querySelector('.search-result--list');
        this.status = document.querySelector('.search-result--title');
        this.progress = document.querySelector('.search-result--progress');
        this.more = document.querySelector('.search-result--more');
        this.input.addEventListener('compositionstart', () => {
            this.composing = true;
            clearTimeout(this.timer);
            this.version++;
        });
        this.input.addEventListener('compositionend', () => {
            this.composing = false;
            this.queueSearch();
        });
        this.input.addEventListener('input', (event: InputEvent) => {
            if (!this.composing && !event.isComposing) this.queueSearch();
        });
        this.form.addEventListener('submit', event => {
            event.preventDefault();
            if (!this.composing) this.queueSearch(true);
        });
        this.more.addEventListener('click', () => this.showMore(this.version, true));
        window.addEventListener('popstate', () => this.readQuery());
        this.readQuery();
    }

    private readQuery() {
        this.input.value = new URL(window.location.href).searchParams.get('keyword') || '';
        this.queueSearch(true);
    }

    private queueSearch(immediate = false) {
        clearTimeout(this.timer);
        const version = ++this.version;
        const query = this.input.value.trim().slice(0, 200);
        const url = new URL(window.location.href);
        if (query) url.searchParams.set('keyword', query);
        else url.searchParams.delete('keyword');
        window.history.replaceState(null, '', url);
        this.results = [];
        this.shown = 0;
        this.list.replaceChildren();
        this.progress.textContent = '';
        this.more.hidden = true;
        this.more.disabled = false;
        this.status.textContent = query ? this.form.dataset.loading : '';
        this.list.setAttribute('aria-busy', String(Boolean(query)));
        if (!query) return;
        if (immediate) void this.search(query, version);
        else this.timer = setTimeout(() => void this.search(query, version), 250);
    }

    private getEngine(): Promise<SearchEngine> {
        if (!this.engine) {
            // Variable import leaves the generated module out of Hugo's bundle.
            const moduleURL = this.form.dataset.module;
            this.engine = import(moduleURL).then(async engine => {
                await engine.options({
                    excerptLength: 35,
                    ranking: { termFrequency: 1, pageLength: 0.5, termSaturation: 1.2 }
                });
                return engine;
            }).catch(error => {
                this.engine = undefined;
                throw error;
            });
        }
        return this.engine;
    }

    private async search(query: string, version: number) {
        try {
            const engine = await this.getEngine();
            if (version !== this.version) return;
            const response = await engine.search(query);
            if (version !== this.version) return;
            this.results = response.results;
            if (!this.results.length) {
                this.status.textContent = this.form.dataset.noResults;
                this.list.setAttribute('aria-busy', 'false');
                return;
            }
            await this.showMore(version);
        } catch {
            if (version === this.version) this.showError();
        }
    }

    private message(template: string) {
        return template.replace('#TOTAL', String(this.results.length)).replace('#SHOWN', String(this.shown));
    }

    private async showMore(version: number, focus = false) {
        if (this.more.disabled || this.shown >= this.results.length) return;
        this.more.disabled = true;
        this.list.setAttribute('aria-busy', 'true');
        try {
            const pages = await Promise.all(
                this.results.slice(this.shown, this.shown + this.pageSize).map(hit => hit.data())
            );
            if (version !== this.version) return;
            const articles = pages.map(page => this.render(page));
            this.list.append(...articles);
            this.shown += articles.length;
            this.status.textContent = this.message(this.form.dataset.summary);
            this.progress.textContent = this.message(this.form.dataset.showing);
            this.more.hidden = this.shown >= this.results.length;
            if (focus) articles[0]?.querySelector('a')?.focus();
        } catch {
            if (version === this.version) this.showError();
        } finally {
            if (version === this.version) {
                this.more.disabled = false;
                this.list.setAttribute('aria-busy', 'false');
            }
        }
    }

    private showError() {
        this.status.textContent = this.form.dataset.error;
        this.list.setAttribute('aria-busy', 'false');
    }

    private render(page: SearchPage): HTMLElement {
        const article = document.createElement('article');
        const link = document.createElement('a');
        link.href = page.url;
        const details = document.createElement('div');
        details.className = 'article-details';
        const title = document.createElement('h2');
        title.className = 'article-title';
        title.textContent = page.meta.title || page.url;
        const preview = document.createElement('section');
        preview.className = 'article-preview';
        // Pagefind escapes content before adding its own <mark> elements.
        preview.innerHTML = page.excerpt;
        details.append(title, preview);
        link.append(details);
        if (page.meta.image) {
            const wrapper = document.createElement('div');
            wrapper.className = 'article-image';
            const image = document.createElement('img');
            image.src = page.meta.image;
            image.alt = '';
            image.width = image.height = 120;
            image.loading = 'lazy';
            image.decoding = 'async';
            wrapper.append(image);
            link.append(wrapper);
        }
        article.append(link);
        return article;
    }
}

const form = document.querySelector<HTMLFormElement>('.search-form:not(.widget)');
if (form) new Search(form);
export default Search;
