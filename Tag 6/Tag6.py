inp = open("input.txt").read()

print(inp)


def solve():
    c = 0
    for e in range(4, len(inp)):
        a = set(inp[e-4:e])
        if len(a) == 4:
            c = e
            break
    return "Aufgabe 1: " + str(c)


print(solve())

def solve2():
    c = 0
    for e in range(14, len(inp)):
        a = set(inp[e-14:e])
        if len(a) == 14:
            c = e
            break
    return "Aufgabe 2: " + str(c)

print(solve2())
