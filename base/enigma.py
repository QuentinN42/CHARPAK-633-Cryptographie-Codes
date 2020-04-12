from .enigma_data import base_gears


class Enigma:
    def __init__(self, gears, keys):
        self.gears, self.keys = [base_gears[g] for g in gears], list(keys)

    def __call__(self, text):
        return "".join(map(self.code_one, text))

    def code_one(self, letter):
        pos = ord(letter)
        for i, k in enumerate(self.keys):
            pos = (self.gears[i][(k + pos) % 256] - k + 256) % 256
        self.rotate()
        return chr(pos)

    def rotate(self):  # maybe while
        self.keys[0] += 1
        if self.keys[0] == 256:
            self.keys[0] = 0
            self.keys[1] += 1
            if self.keys[1] == 256:
                self.keys[1] = 0
                self.keys[2] += 1
                if self.keys[2] == 256:
                    self.keys[2] = 0


class EnigmaDecode(Enigma):
    def code_one(self, letter):
        pos = ord(letter)
        for i, k in reversed(list(enumerate(self.keys))):
            pos = (self.gears[i].index((pos + k) % 256) - k + 256) % 256
        self.rotate()
        return chr(pos)
