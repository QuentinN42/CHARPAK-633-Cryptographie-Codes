"""
Basic auto cipher and decipher
"""
from .functions import search_shift, search_vignere, search_transpose, zipMerge
from .abstract_classes import Shift, Transpose, LinspaceCut, MultiFunc


def decipher(filename: str, dec: callable):
    with open(filename, "r", encoding='utf8') as f:
        content = f.read()

    result = dec(content)

    return result


def auto_shift(filename: str):
    with open(filename, "r", encoding='utf8') as f:
        content = f.read()

    result = Shift(search_shift(content))(content)

    return result


def auto_vignere(filename: str, n: int = None):
    with open(filename, "r", encoding='utf8') as f:
        content = f.read()

    if n:
        k = search_vignere(content, n)
    else:
        k = search_vignere(content)
    print(f"Detected: {k}")
    result = Vignere(k)(content)

    return result


def auto_transpose(filename: str):
    with open(filename, "r", encoding='utf8') as f:
        content = f.read()

    k = search_transpose(content)
    print(f"Detected: {k}")
    if k != 0:
        return Transpose(k)(content)

    return content


def auto_vignere_t(content: str):

    k = search_vignere(content)
    print(f"Detected: {k}")
    result = Vignere(k)(content)

    return result


def auto_transpose_t(content: str):

    k = search_transpose(content)
    print(f"Detected: {k}")
    if k != 0:
        return Transpose(k)(content)

    return content


class Vignere:
    def __init__(self, nb_cle: int):
        self.nb_cle = nb_cle

    def __call__(self, content):
        cut = LinspaceCut(self.nb_cle)
        keys = map(search_shift, cut(content))
        funcs = map(Shift, keys)
        return MultiFunc(cut, funcs, zipMerge)(content)
