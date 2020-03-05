"""
Some functions to edit strings
"""
import numpy as np
from sklearn.metrics import r2_score
from tqdm import tqdm

from .abstract_classes import LinspaceCut, Transpose
from .const import letter_frequency, word_frequency


def r2(a, b):
    _a = a[:min(len(a), len(b))]
    _b = b[:min(len(a), len(b))]
    return r2_score(_a, _b)


def frequency(txt: str):
    """
    extract number of letters for each letters
    :param txt:
    :return: dict of frequency
    >>> frequency('bienvenue') == {'b' : 1, 'i' : 1, 'e' : 3, 'n' : 2, 'v' : 1, 'u' : 1}
    True
    """
    return {c: txt.count(c) for c in set(txt)}


def word_len_frequency_dict(txt):
    txt = txt.replace("\n", " ")
    while "  " in txt:
        txt = txt.replace("  ", " ")
    splited = txt.split(" ")
    le = len(splited)
    di = {w: splited.count(w)/le for w in set(splited)}
    return di


def search_shift(txt: str) -> int:
    """
    get the most frequent letter
    assuming this letter is SPACE
    find the shift from this letter
    >>> search_shift('aaa')
    -65
    >>> search_shift('   ')
    0
    """
    freqs = frequency(txt)
    letter = max(freqs.keys(), key=lambda x: freqs[x])
    shift = ord(" ") - ord(letter)
    return shift


def search_vignere(txt: str, n: int = 50) -> int:
    """
    list all frequencies for a cut from 1 to n
    calculate r2 for each split
    return the best r2 index
    """
    _range = range(1, n + 1)
    cutters = map(LinspaceCut, _range)
    txts = [cut(txt)[0] for cut in cutters]
    print("Vignere test :")
    freqs = [np.array(sorted(frequency(tx).values(), reverse=True)[1:])/len(tx) for tx in tqdm(txts)]
    r2s = [r2(letter_frequency, f) for f in freqs]
    cle = max(_range, key=lambda i: r2s[i-1])
    return cle


def search_transpose(txt: str) -> int:
    def test_transpose(dec, text):
        txt_tr = Transpose(dec)(text)
        tmp = word_len_frequency_dict(txt_tr)
        ks = tmp.keys()
        return [tmp[k] if k in ks else 0 for k in word_frequency.keys()]

    first = list(word_frequency.values())
    print("Transpose test :")
    r2s = [r2(first, test_transpose(i, txt)) for i in tqdm(range(1, len(txt)))]
    m = max(range(1, len(txt)), key=lambda i: r2s[i - 1])
    return m if r2s[m - 1] > 0.7 else 0


def simpleMerge(l: list):
    return "".join(l)


def zipMerge(l: list):
    """
    >>> zipMerge(["abc", "abc", "a"]) == 'aaabbcc'
    True
    """
    max_len = max(map(len, l))
    _out = ""
    for j in range(max_len):
        for i in range(len(l)):
            if j < len(l[i]):
                _out += l[i][j]
    return _out
