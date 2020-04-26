#!/usr/bin/env python3
import sys

PREC = {
    "+": (2, 0),
    "*": (1, 0),
}

def fn(x):
    return {
        "+": lambda x, y: x + y,
        "*": lambda x, y: x * y,
    }[x]

def csflush(sn, st, cs):
    if len(cs) > 0:
        st += [int("".join(cs))]
        sn[-1] += 1
        cs.clear()

def syflush(sn, st, syn, sy, lvl):
    for i in range(syn[-1]):
        assert sy and syn[-1] > 0
        if sy[-1][1] > lvl:
            break

        R = st.pop()
        H = sy.pop()[0]
        L = st.pop()
        L = fn(H)(L, R)
        st += [L]

        syn[-1] -= 1
        sn[-1] -= 1

#        st += [sy.pop()[0]]
#        sn[-1] += 1
#        syn[-1] -= 1


if __name__ == "__main__":
    x = " ".join(sys.argv[1:])

    sn, spushed, st  = [0], [0], []
    syn, sy = [0], []
    cs = []

    y = None
    for c in x + "\0":

        # LEX
        if c == " ":
            continue
        if "0" <= c <= "9":
            cs += [c]
            continue
        elif len(cs) > 0:
            csflush(sn, st, cs)

        # PARSE
        parity = (sn[-1] + spushed[-1] + syn[-1]) % 2

        if c in ";|)\0":
            if parity == 0:
                sn[-1] += 1
                st += [0]
            syflush(sn, st, syn, sy, 100)

        if c == ";":
            for _ in range(sn[-1]):
                st.pop()
            sn[-1] = spushed[-1] = 0
            continue
        elif c == "|":
            spushed[-1] += 1
            continue
        elif c == "(":
            sn[-1] += 1
            # TODO increase syn?
            sn += [0]
            spushed += [0]
            syn += [0]
            continue
        elif c in ")\0":
            spushed.pop()
            syn.pop()
            sn.pop()
            continue

        elif c == "_":
            # TODO only odd parity?
            v = 0 if sn[-1] == 0 else st[-1]
            st += [v]
            sn[-1] += 1
            continue

        elif c in "+*":
            if parity == 1:
                prec, right = PREC[c]
                syflush(sn, st, syn, sy, prec)
                sy += [(c, prec - right)]
                syn[-1] += 1
            else:
                st += [c]
                st[-1] += 1
        else:
            assert False


    print("---")
    print(x)
    print(st)
