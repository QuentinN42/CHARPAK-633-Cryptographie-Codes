alphabet = "abcdefghijklmnopqrstuvwxyz"


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
    'qrs'
    >>> Shift(15)("abc")
    'pqr'
    >>> Shift(2)("abcdefghijklmnopqrstuvwxyz")
    'cdefghijklmnopqrstuvwxyzab'
    """
    def __init__(self, dec: int):
        _dic: dict = {e: nl(((ln(e)+dec-1) % 26)+1) for e in alphabet}
        self.func = Switch(_dic)

    def __call__(self, _in):
        _out = self.func(_in)
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
