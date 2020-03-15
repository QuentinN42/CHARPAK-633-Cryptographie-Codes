from base import EnigmaDecode as De

tests = [
    ([5, 7, 2], [188, 22, 57]),
    ([3, 2, 6], [40, 143, 67]),
    ([6, 3, 5], [226, 165, 83]),
    ([6, 5, 3], [67, 170, 206]),
    ([6, 2, 1], [235, 149, 214])
]


with open("data/message8.txt", "r") as f:
    content = f.read()


for g,p in tests:
    de = De(g, p)
    print(g,p)
    print(de(content)[-10:])

