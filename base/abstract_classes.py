"""
Abstract decipher classes
"""


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
        _out = "".join([chr(ord(e) + self.dec) for e in _in])
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
        _out = "".join([_in[i :: self.n] for i in range(self.n)])
        return _out


class LinspaceCut:
    def __init__(self, n):
        self.n = n

    def __call__(self, _in):
        return [_in[i :: self.n] for i in range(self.n)]


class MultiFunc:
    def __init__(self, cutter, funcs, merger):
        self.cutter = cutter
        self.funcs = funcs
        self.merger = merger

    def __call__(self, _in):
        _out = "".join(
            self.merger([f(sub_in) for f, sub_in in zip(self.funcs, self.cutter(_in))])
        )
        return _out
