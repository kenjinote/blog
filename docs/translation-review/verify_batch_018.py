"""Validate explicitly reviewed primality article versions; never record prose reviews."""
import argparse
import hashlib
import importlib.util
import json
import random
import re
import subprocess
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FOLDER = ROOT / 'content/post/cppで実装する高速な素数判定アルゴリズム'
SLUG = 'cpp-fast-prime-testing-miller-rabin'
spec = importlib.util.spec_from_file_location('rendering', Path(__file__).with_name('verify_batch_013_rendering.py'))
rendering = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rendering)


def digest(path):
    return hashlib.sha256(path.read_text(encoding='utf-8-sig').replace('\r\n', '\n').encode()).hexdigest()


def sieve(limit):
    flags = bytearray(b'\1') * (limit + 1)
    flags[0:2] = b'\0\0'
    for p in range(2, int(limit ** .5) + 1):
        if flags[p]:
            flags[p*p::p] = b'\0' * ((limit - p*p) // p + 1)
    return flags


def reference_prime(n):
    """Independent Python pow arithmetic and first twelve prime bases, range <2^64.

    Relies on the published twelve-base bound; not an independent proof of that bound.
    """
    if n < 2:
        return False
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n == a:
            return True
        if n % a == 0:
            return False
    d, s = n - 1, 0
    while not d & 1:
        d //= 2
        s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        residues = [pow(a, d * 2**r, n) for r in range(s)]
        if residues[0] != 1 and n - 1 not in residues:
            return False
    return True


def cases():
    flags = sieve(50000)
    commands, expected = [], []
    for n, prime in enumerate(flags):
        for mode in ('P', 'T'):
            commands.append(f'{mode} {n}')
            expected.append(str(prime))
    for n in (-2**63, -9, -1, 2**63-1):
        commands.append(f'T {n}')
        expected.append('0')
    rng = random.Random(20261028)
    large = {0, 1, 2, 3, 61, 73, 325, 341, 561, 1105, 1729, 2047,
             1373653, 25326001, 3215031751, 341550071728321, 3825123056546413051,
             1000000007, 998244353, 1000000000000000003, 1000000000000000007,
             18446744073709551557, 2**63-1, 2**64-1}
    for threshold in (4759123141, 1122004669633):
        large.update(range(threshold-3, threshold+4))
    for bits in range(1, 65):
        large.update(n for n in (2**bits-1, 2**bits, 2**bits+1) if n < 2**64)
    large.update(rng.getrandbits(64) for _ in range(512))
    for p in (1000000007, 1000000009, 2147483647, 4294967291):
        for q in (1000000007, 2147483647, 4294967291):
            large.add(p*q)
    for n in sorted(large):
        commands.append(f'P {n}')
        expected.append(str(int(reference_prime(n))))
    for _ in range(256):
        a, b, m = rng.getrandbits(64), rng.getrandbits(64), rng.randrange(1, 2**64)
        commands.append(f'M {a} {b} {m}')
        expected.append(str(a*b % m))
        commands.append(f'E {a} {b} {m}')
        expected.append(str(pow(a, b, m)))
    for a, b, m in ((0, 0, 1), (0, 0, 7), (2, 0, 1), (2, 0, 7),
                    (2**64-1, 2**64-1, 2**64-1), (2**64-1, 2**64-1, 2**64-59)):
        commands.extend((f'M {a} {b} {m}', f'E {a} {b} {m}'))
        expected.extend((str(a*b % m), str(pow(a, b, m))))
    commands.extend(('M 1 2 0', 'E 2 3 0', 'E 2 0 0'))
    expected.extend(('ERROR',) * 3)
    return commands, expected, {'sieveRange': [0, 50000], 'sieveCasesPerAlgorithm': 50001,
                                'extraSignedTrialCases': 4, 'largeAndBoundaryMillerRabinCases': len(large),
                                'multiplicationCases': 262, 'powerCases': 262, 'zeroModulusCases': 3}


def unix(path):
    value = path.resolve().as_posix()
    return '/mnt/' + value[0].lower() + value[2:]


def compile_code(source, tmp, name, flags=None):
    path, binary = tmp / (name + '.cpp'), tmp / name
    path.write_text(source, encoding='utf-8')
    command = ['wsl', '--exec', 'g++', '-std=c++17', '-Wall', '-Wextra', *(flags or ['-O2']), unix(path), '-o', unix(binary)]
    result = subprocess.run(command, capture_output=True, text=True, encoding='utf-8', timeout=90)
    assert result.returncode == 0, result.stderr
    assert not result.stderr.strip(), result.stderr
    return binary


def execute(binary, input_text=''):
    result = subprocess.run(['wsl', '--exec', unix(binary)], input=input_text, capture_output=True,
                            text=True, encoding='utf-8', timeout=60)
    assert result.returncode == 0 and not result.stderr, result.stderr
    return result.stdout.splitlines()


def verify(site, languages):
    commands, expected, counts = cases()
    tmp = Path(tempfile.mkdtemp(prefix='kenji-batch018-', dir=Path.home()/'.codex/tmp'))
    source = (FOLDER/'index.md').read_text(encoding='utf-8')
    source_blocks = re.findall(r'^```cpp\n(.*?)^```', source, re.M | re.S)
    source_displays = re.findall(r'^\$\$\n(.*?)^\$\$', source, re.M | re.S)
    assert len(source_blocks) == 3 and len(source_displays) == 4
    external = {'https://cacr.uwaterloo.ca/hac/about/chap4.pdf',
                'https://math.nyu.edu/~goodman/teaching/Algebra_2_2021/MillerRabinTest.pdf',
                'https://miller-rabin.appspot.com/', 'https://arxiv.org/abs/1509.00864',
                'https://gcc.gnu.org/onlinedocs/gcc/_005f_005fint128.html',
                'https://eel.is/c++draft/expr.mul', 'https://cacr.uwaterloo.ca/hac/about/chap14.pdf'}
    harness = r'''
int main() {
    char mode;
    while (std::cin >> mode) {
        try {
            if (mode == 'T') {
                std::int64_t n; std::cin >> n;
                std::cout << is_prime_trial_division(n) << '\n';
            } else if (mode == 'P') {
                u64 n; std::cin >> n; std::cout << is_prime_miller_rabin(n) << '\n';
            } else {
                u64 a,b,m; std::cin >> a >> b >> m;
                std::cout << (mode == 'M' ? mod_mul(a,b,m) : mod_pow(a,b,m)) << '\n';
            }
        } catch (const std::invalid_argument&) { std::cout << "ERROR\n"; }
    }
}'''
    files = []
    for lang in languages:
        path = FOLDER / ('index.md' if lang == 'ja' else 'index.'+lang+'.md')
        text = path.read_text(encoding='utf-8')
        blocks = re.findall(r'^```cpp\n(.*?)^```', text, re.M | re.S)
        assert blocks == source_blocks, 'Executable blocks differ: ' + lang
        assert re.findall(r'^\$\$\n(.*?)^\$\$', text, re.M | re.S) == source_displays
        assert len(re.findall(r'^## [1-7]\. ', text, re.M)) == 7
        diagrams = re.findall(r'^```mermaid\n(.*?)^```', text, re.M | re.S)
        assert [len(re.findall(r'--(?: [^\n]*?)?\s*>', diagram)) for diagram in diagrams] == [14, 4]
        assert re.search(r'More -- [^\n]+ --> Fail', diagrams[0]) and 'Next --> More' in diagrams[0]
        links = re.findall(r'\]\((https://[^)]+)\)', text)
        assert {u for u in links if not u.startswith('https://kenji.blog/')} == external
        internal = 'https://kenji.blog/' + ('' if lang == 'ja' else lang+'/') + 'p/modern-cryptography-public-key-hash-signature/'
        assert [u for u in links if u.startswith('https://kenji.blog/')] == [internal]
        assert (site/internal.removeprefix('https://kenji.blog/')/'index.html').is_file()
        for marker in ('date: "2026-09-11T14:00:00+09:00"', 'lastmod: "2026-10-28"',
                       f'slug: "{SLUG}"', 'image: "img/eyecatch.jpg"'):
            assert marker in text
        assert (FOLDER/'img/eyecatch.jpg').is_file()
        main = compile_code(blocks[2], tmp, lang+'-main')
        samples = [0,1,2,73,561,1000000007,998244353,1000000000000000003,
                   1000000000000000007,18446744073709551557,2**64-1]
        assert execute(main) == [str(n)+' is '+('Prime' if reference_prime(n) else 'Not prime') for n in samples]
        # Compile each fragment separately with a minimal driver; the complete program already contains helpers.
        compile_code(blocks[0]+'\nint main(){return is_prime_trial_division(2)?0:1;}\n', tmp, lang+'-trial')
        helper = compile_code(blocks[1]+'\nint main(){return mod_pow(2,0,1)==0?0:1;}\n', tmp, lang+'-helper')
        execute(helper)
        combined = blocks[2].split('int main()')[0] + blocks[0] + harness
        for name, flags in [('optimized',['-O2']), ('ubsan',['-O1','-fsanitize=undefined','-fno-sanitize-recover=undefined'])]:
            binary = compile_code(combined, tmp, lang+'-'+name, flags)
            actual = execute(binary, '\n'.join(commands)+'\n')
            assert actual == expected, f'{lang} {name}: first mismatch '+str(next(((i,a,b) for i,(a,b) in enumerate(zip(actual,expected)) if a != b), 'length'))
        prose = re.sub(r'^```.*?^```[^\n]*', '', text, flags=re.M | re.S)
        html = (site/('' if lang == 'ja' else lang)/'p'/SLUG/'index.html').read_text(encoding='utf-8')
        parser = rendering.ArticleText(); parser.feed(html); rendered = ''.join(parser.parts)
        expected_math, actual_math = rendering.expressions(prose), rendering.expressions(rendered)
        assert expected_math == actual_math, (expected_math-actual_math, actual_math-expected_math)
        assert all(u in html for u in links)
        assert 'katex' in html and 'mermaid' in html
        assert r'0\le N<2^{64}' in actual_math
        files.append({'language':lang,'path':path.relative_to(ROOT/'content').as_posix(),'hash':digest(path),
                      'codeBlocks':3,'displayFormulas':4,'texExpressions':sum(expected_math.values()),
                      'diagramEdges':[14,4],'primaryReferenceTargets':7,'sampleOutputs':11,
                      'casesPerHarness':len(commands),'optimizedAndUbsanPassed':True,'allTeXPreserved':True,'passed':True})
    assert pow(3,560,561)==375
    assert 318665857834031151167461 > 2**64
    return {'version':1,'checkedAt':datetime.now(timezone(timedelta(hours=9))).isoformat(),
            'site':str(site),'compiler':'WSL GCC13.3.0/C++17','tempDirectory':str(tmp),'scope':'Only explicitly selected languages; not an automated prose review or review-date recorder.',
            'counts':counts,'files':files,'allPassed':True,
            'limitations':['Finite tests, not an independent exhaustive64bit base-set proof.','Large-number reference uses independent Python pow and published first12prime-base bound.','No timing, native-language, visual-browser, constant-time or cryptographic-library certification.']}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('site', type=Path)
    parser.add_argument('--languages', nargs='+', required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        parser.error('Preserve existing evidence; use a new output path.')
    result = verify(args.site, args.languages)
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'versions':len(result['files']),'casesPerVersionPerBuild':result['files'][0]['casesPerHarness'],
                      'texExpressions':sum(f['texExpressions'] for f in result['files']),'passed':True}))
