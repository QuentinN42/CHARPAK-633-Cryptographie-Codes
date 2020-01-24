

class Shift:
    def __init__(self, dec):
        pass

    def __call__(self, _in):
        _out = _in  # TODO: add func
        return _out


class Switch:
    def __init__(self, dic):
        self.dic: dict = dic

    def __call__(self, _in):
        _out = "".join([self.dic[e] if e in self.dic.keys() else e for e in _in])
        return _out
