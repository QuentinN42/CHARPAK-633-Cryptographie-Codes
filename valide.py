from set import get_json, get_keys
import os


length = 99115


def reverse(poss):
    for i in range(length - 7):
        poss[0] -= 1
        if poss[0] == -1:
            poss[0] = 255
            poss[1] -= 1
            if poss[1] == -1:
                poss[1] = 255
                poss[2] -= 1
                if poss[2] == -1:
                    poss[2] = 255
    return poss

if __name__ == "__main__":
    for f in os.listdir("./results/"):
        ln = "./results/" + f
        data = get_json(ln)
        for poss in data:
            print(f"Gears [{f[3:].replace('_',', ')}] at pos [{', '.join(map(str,reverse(get_keys(poss))))}]")

