"""
Basic auto cipher and decipher
"""
from .abstract_classes import Shift, MultiFunc, LinspaceCut
from .functions import search_shift, zipMerge


def decipher(filename: str, dec: callable):
    with open(filename, "r") as f:
        content = f.read()

    result = dec(content)

    return result


def cipher(filename: str, cip: callable):
    with open(filename, "r") as f:
        content = f.read()

    result = cip(content)

    return result


def auto_shift(filename: str):
    with open(filename, "r") as f:
        content = f.read()

    result = Shift(search_shift(content))(content)

    return result


def vignere(filename: str, nb_cle: int):
    with open(filename, "r") as f:
        content = f.read()

    cut = LinspaceCut(nb_cle)
    keys = map(search_shift, cut(content))
    funcs = map(Shift, keys)
    return decipher(filename, MultiFunc(cut, funcs, zipMerge))
