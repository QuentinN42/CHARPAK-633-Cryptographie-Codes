"""
Basic auto cipher and decipher
"""
from .functions import search_shift, search_vignere, zipMerge
from .abstract_classes import Shift, LinspaceCut, MultiFunc


def decipher(filename: str, dec: callable):
    with open(filename, "r") as f:
        content = f.read()

    result = dec(content)

    return result


def auto_shift(filename: str):
    with open(filename, "r") as f:
        content = f.read()

    result = Shift(search_shift(content))(content)

    return result


def auto_vignere(filename: str):
    with open(filename, "r") as f:
        content = f.read()

    result = Vignere(search_vignere(content))(content)

    return result


class Vignere:
    def __init__(self, nb_cle: int):
        self.nb_cle = nb_cle

    def __call__(self, content):
        cut = LinspaceCut(self.nb_cle)
        keys = map(search_shift, cut(content))
        funcs = map(Shift, keys)
        return MultiFunc(cut, funcs, zipMerge)(content)
