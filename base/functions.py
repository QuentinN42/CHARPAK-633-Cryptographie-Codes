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


def ln(char: str):
    """
    letter to number
    :param char: a character
    :return numb: a number
    >>> ln("a")
    1
    >>> ln("r")
    18
    """
    numb = ord(char.lower()) - 96
    return numb


def nl(numb: int):
    """
    number to letter
    :param numb: a number
    :return char: a character
    >>> nl(23)
    'w'
    >>> nl(3)
    'c'
    """
    char = chr(numb + 96)
    return char


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
