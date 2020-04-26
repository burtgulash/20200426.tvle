#!/usr/bin/env python3
import sys

def fn(x):
    return {
        "+": lambda x, y: x + y,
        "*": lambda x, y: x * y,
    }[x]

def flush(st, sy):
    while sy:
        st += [sy.pop()]

def ex(xs):
    ys = []
    for x in xs:
        if isinstance(x, int):
            ys += [x]
        elif isinstance(x, str):
            R = ys.pop()
            L = ys.pop()
            y = fn(x)(L, R)
            ys += [y]
    return ys


if __name__ == "__main__":
    x = " ".join(sys.argv[1:])
    print(x)


    st = []
    sy = []

    y = None
    for c in x:
        if "0" < c < "9":
            st += [int(c)]
        elif c in "+*":
            flush(st, sy)
            sy += [c]
    flush(st, sy)

    print(st)

    y = ex(st)
    print(y)
