"""
Some functions to edit strings
"""


def frequency(txt: str):
    """
    extract number of letters for each letters
    :param txt:
    :return: dict of frequency
    >>> frequency('bienvenue') == {'b' : 1, 'i' : 1, 'e' : 3, 'n' : 2, 'v' : 1, 'u' : 1}
    True
    """
    return {c: txt.count(c) for c in set(txt)}


def search_shift(txt: str):
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
