from set import test, get_json
import sys


gs = get_json(sys.argv[1])

test(gs)
