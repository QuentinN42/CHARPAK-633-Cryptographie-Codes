import argparse
from base import auto_vignere


class Args:
    def __init__(self):
        parser = argparse.ArgumentParser()

        # Positional mandatory arguments
        parser.add_argument("path", help="The file path.", type=str)

        # Optional arguments
        parser.add_argument("-o", "--output", help="Write output in a file.", type=str)

        self.args = parser.parse_args()

    @property
    def path(self):
        return self.args.path

    @property
    def output(self):
        return self.args.output

    def _out(self, msg: str):
        if self.output:
            with open(self.output, "w") as f:
                f.write(msg + "\n")
        else:
            print(msg)

    def run(self):
        self._out(auto_vignere(self.path))


if __name__ == "__main__":
    Args().run()
