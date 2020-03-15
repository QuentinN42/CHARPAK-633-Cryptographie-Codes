from base import EnigmaDecode, base_gears
from tqdm import tqdm
import json


txt = "".join(map(chr, [185, 183, 38, 100, 59, 37, 72]))


def get_json(link: str) -> dict:
    return json.load(open(link, "r"))


def write_json(link: str, data) -> None:
    _json = json.dumps(data, sort_keys=True, separators=(",", ": "))
    with open(link, "w") as f:
        for l in _json.split("\n"):
            f.write(l + "\n")


def get_keys(n):
    return [(n%256)%256, (n//256)%256, (n//256)//256]


def test(gearss):
    length = len(gearss)
    for i, gears in enumerate(gearss):
        print(f"{i}/{length}")
        out = test_one(gears)
        print(f"{out} 'Joël\\n' found.")


def test_one(gears):
    res = list(filter(lambda x: "Joël" in EnigmaDecode(gears, get_keys(x))(txt), tqdm(range(256**3))))
    ln = "results/res" + "_".join(map(str,gears))
    write_json(ln, res)
    return len(res)

