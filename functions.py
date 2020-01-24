

class Shift:
    def __init__(self, dec):
        pass

    def __call__(self, _in):
        _out = _in  # TODO: add func
        return _out


class Switch:
    def __init__(self, dic):
        self.dic = dic

    def __call__(self, _in):
        _out = _in  # TODO: dic[e] for e in _in
        return _out
