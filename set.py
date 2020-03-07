from base import EnigmaDecode, base_gears
from tqdm import tqdm
import json


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
    res = list(filter(lambda x: EnigmaDecode(gears, get_keys(x))("&d;%H") == "Joël\n", tqdm(range(256**3))))
    write_json("results/res" + "_".join(gears), res)
    return len(res)
