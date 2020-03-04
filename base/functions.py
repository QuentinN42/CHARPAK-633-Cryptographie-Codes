"""
Some functions to edit strings
"""
import numpy as np
from sklearn.metrics import r2_score

from .abstract_classes import LinspaceCut
from .const import th


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
    freqs = [np.array(sorted(frequency(tx).values(), reverse=True)[1:])/len(tx) for tx in txts]
    r2s = [r2(t, f) for t, f in zip([th] * len(freqs), freqs)]
    cle = max(_range, key=lambda i: r2s[i-1])
    return cle


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
