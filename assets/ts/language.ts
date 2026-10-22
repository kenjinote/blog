// Runs with defer, independently of image, analytics and advertisement loading.
const languageSelect = document.querySelector<HTMLSelectElement>("#language-select");
const languageStatus = document.querySelector<HTMLElement>("#language-status");
if (languageSelect && languageStatus) {
    languageSelect.disabled = false;
    languageSelect.addEventListener("change", () => {
        const option = languageSelect.selectedOptions[0];
        if (option.value) {
            window.location.assign(option.value);
            return;
        }
        languageStatus.querySelector("p")!.textContent = languageStatus.dataset.missing!;
        languageStatus.querySelector<HTMLAnchorElement>("a")!.href = option.dataset.home!;
        const languageName = languageStatus.querySelector<HTMLElement>("[data-language-name]")!;
        languageName.textContent = option.textContent!.split(" — ")[0];
        languageName.lang = option.dataset.language!;
        languageStatus.hidden = false;
        // The selected language must continue to describe the article being read.
        languageSelect.value = Array.from(languageSelect.options).find(
            item => item.dataset.language === languageSelect.dataset.currentLanguage
        )!.value;
    });
}
