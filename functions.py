"""
Some functions to edit strings
"""
alphabet = "abcdefghijklmnopqrstuvwxyz"


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
    assuming this letter is 'e' (most frequent in french)
    find the shift from this letter
    >>> search_shift('aaa')
    4
    >>> search_shift('eee')
    0
    """
    freqs = frequency(txt)
    letter = max(freqs.keys(), key=lambda x: freqs[x])
    shift = ln('e') - ln(letter)
    return shift


def auto_shift(txt: str):
    return Shift(search_shift(txt))(txt)


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


class Shift:
    """
    >>> Shift(-10)("abc")
    'WXY'
    >>> Shift(15)("abc")
    'pqr'
    >>> Shift(2)("abcdefghijklmnopqrstuvwxyz")
    'cdefghijklmnopqrstuvwxyz{|'
    """
    def __init__(self, dec: int):
        self.dec: int = dec

    def __call__(self, _in):
        _out = "".join([chr(ord(e)+self.dec) for e in _in])
        return _out


class Switch:
    """
    >>> Switch({"a":"b", "b":"a"})("aabb")
    'bbaa'
    """
    def __init__(self, dic: dict):
        self.dic: dict = dic

    def __call__(self, _in):
        _out = "".join([self.dic[e] if e in self.dic.keys() else e for e in _in])
        return _out


class Transpose:
    """
    >>> Transpose(2)("abcd")
    'acbd'
    """
    def __init__(self, n: int):
        self.n: int = n

    def __call__(self, _in):
        _out = "".join([_in[i::self.n] for i in range(self.n)])
        return _out
