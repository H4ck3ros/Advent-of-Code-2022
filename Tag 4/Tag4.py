inp = open("input.txt").read().split("\n")
summe = [0]


def convert(x, y):
    test1 = []
    test2 = []
    x1, x2 = x.split("-")
    y1, y2 = y.split("-")
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    for i in range(x1, x2 + 1):
        test1.append(i)

    for i in range(y1, y2 + 1):
        test2.append(i)


    zerg = [test1, test2]

    return equal(zerg, x1, x2, y1, y2)


def equal(x, x1, x2, y1, y2):
    twerg = {}
    twerg2 = {}
    #if x1 != x2 and y1 != y2:
    for i in range(x1, x2 + 1):
        if i not in x[1]:
            twerg[i] = False
            break

        twerg[i] = True

    for i in range(y1, y2 + 1):
        if i not in x[0]:
            twerg2[i] = False
            break
        twerg2[i] = True
    if any((any(twerg.values()), any(twerg2.values()))):
        return summe.append(1)
    """else:
        for i in range(x1, x2 + 1):
            if i in x[1]:
                return summe.append(1)

        for i in range(y1, y2 + 1):
            if i in x[0]:
                return summe.append(1)"""


def solve():
    for i in range(len(inp)):
        check = inp[i]
        checkhelp = check.split(",")
        check1 = checkhelp[0]
        check2 = checkhelp[1]
        convert(check1, check2)
    return sum(summe)


print(solve())
"""def convert(x, y):
    test1 = ""
    test2 = ""
    x1, x2 = x.split("-")
    y1, y2 = y.split("-")
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    for i in range(x1 - 1):
        test1 += "."

    for i in range(x1, x2 + 1):
        test1 += str(i)

    for i in range(0, 9 - len(test1)):
        test1 += "."

    for i in range(y1 - 1):
        test2 += "."

    for i in range(y1, y2 + 1):
        test2 += str(i)

    for i in range(0, 9 - len(test2)):
        test2 += "."

    zerg = [test1, test2]

    return equal(zerg, x1, x2, y1, y2)
    
    def equal(x, x1, x2, y1, y2):
    print(x)
    twerg = {}
    twerg2 = {}
    if x1 != x2 and y1 != y2:

        for i in range(x1, x2 + 1):
            if i != ".":
                if str(i) not in x[1]:
                    twerg[i] = False
                    continue

                twerg[i] = True

        for i in range(y1, y2 + 1):
            if i != ".":
                if str(i) not in x[0]:
                    twerg2[i] = False
                    continue
                twerg2[i] = True

        return find(twerg, twerg2)

    else:
        for i in range(x1, x2 + 1):
            if i != ".":
                if str(i) not in x[1]:
                    break
            return summe.append(1)

        for i in range(y1, y2 + 1):
            if i != ".":
                if str(i) not in x[0]:
                    break
            return summe.append(1)

    def find(x, y):
    print(x,y)
    if len(x.keys()) == len(y.keys()):  # wenn länge gleich
        if False in x.values() or False in y.values():
            return
        return summe.append(1)

    else:
        if len(x.keys()) > len(y.keys()):  # wenn 1 länger ist
            if False in y.values():
                return
            return summe.append(1)
        if len(x.keys()) < len(y.keys()):
            if False in x.values():
                return
            return summe.append(1)"""
