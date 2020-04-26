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

def flush(st, syn, sy):
    for i in range(syn[-1]):
        assert sy
        st += [sy.pop()]
        syn[-1] -= 1

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


    sn, st  = [0], []
    syn, sy = [0], []
    cs = []

    y = None
    for c in x + "\0":
        sn[-1] += 1
        #print("st:", st)

        if "0" <= c <= "9":
            cs += [c]
        elif len(cs) > 0:
            csflush(st, cs)

        if c in "+*":
            flush(st, syn, sy)
            sy += [c]
            syn[-1] += 1

        if c == "(":
            sn += [0]
            syn += [0]

        if c in ")\0":
            csflush(st, cs)
            flush(st, syn, sy)
            syn.pop()
            sn.pop()

    print("---")
    print(st)

    y = ex(st)
    print(y)
