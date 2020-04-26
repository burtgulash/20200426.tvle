#!/usr/bin/env python3
import sys

def fn(x):
    return {
        "+": lambda x, y: x + y,
        "*": lambda x, y: x * y,
    }[x]

def csflush(st, cs):
    if len(cs) > 0:
        st += [int("".join(cs))]
        cs.clear()

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
    cs = []

    y = None
    for c in x:
        if "0" <= c <= "9":
            cs += [c]
        elif len(cs) > 0:
            csflush(st, cs)

        if c in "+*":
            flush(st, sy)
            sy += [c]

    csflush(st, cs)
    flush(st, sy)

    print(st)

    y = ex(st)
    print(y)
