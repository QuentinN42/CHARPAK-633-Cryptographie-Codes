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
    def __init__(self, dec):
        pass

    def __call__(self, _in):
        _out = _in  # TODO: add func
        return _out


class Switch:
    def __init__(self, dic: dict):
        self.dic: dict = dic

    def __call__(self, _in):
        _out = "".join([self.dic[e] if e in self.dic.keys() else e for e in _in])
        return _out
