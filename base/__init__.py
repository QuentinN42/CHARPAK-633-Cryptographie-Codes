

def decipher(filename: str, dec: callable):
    with open(filename, "r") as f:
        content = f.read()

    result = dec(content.lower())

    return result


def cipher(filename: str, cip: callable):
    with open(filename, "r") as f:
        content = f.read()

    result = cip(content.lower())

    return result
