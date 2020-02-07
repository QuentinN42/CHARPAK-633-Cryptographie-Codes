

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
