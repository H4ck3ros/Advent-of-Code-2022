import string

inp = open("input.txt").read().split("\n")

container = []
anweisung = []


def solve():
    for i in inp:
        if "[" in i:
            container.append(i)
            continue
        anweisung.append(i)

    stack = {}
    for e in container[::-1]:
        for i in range(0, int((len(e) + 1) / 4)):
            if e[(i * 4) + 1] != " ":
                if i + 1 not in stack:
                    stack[i + 1] = [e[(i * 4) + 1]]
                else:
                    stack[i + 1].append(e[(i * 4) + 1])
    for e in anweisung[2:]:
        a = e.split(" ")[1::2]
        for j in range(int(a[0])):
            s = stack[int(a[1])].pop()
            stack[int(a[2])].append(s[0])
    for e in stack.values():
        print(e.pop(), end="")
    return ""


print(solve())

def solve2():
    anweisung = []
    for i in inp:
        if "[" in i:
            container.append(i)
            continue
        anweisung.append(i)

    stack = {}
    for e in container[::-1]:
        for i in range(0, int((len(e) + 1) / 4)):
            if e[(i * 4) + 1] != " ":
                if i + 1 not in stack:
                    stack[i + 1] = [e[(i * 4) + 1]]
                else:
                    stack[i + 1].append(e[(i * 4) + 1])
    for e in anweisung[2:]:
        a = e.split(" ")[1::2]
        k =[]
        for j in range(int(a[0])):
            s = stack[int(a[1])].pop()
            k.append(s[0])
        stack[int(a[2])].extend(k[::-1])
    for e in stack.values():
        print(e.pop(), end="")
    return ""

print(solve2())