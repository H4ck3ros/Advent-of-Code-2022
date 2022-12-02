inp = open("input.txt").read().split("\n")


def solve():
    erg = []
    choose = []
    for i in range(len(inp)):
        check = tuple(inp[i])
        check = check[::2]
        if len(check) != 2:
            continue
        if check[0] == "A":  # wenn rock
            if check[1] == "X":
                erg.append("D")
                choose.append("R")
            elif check[1] == "Y":
                erg.append("W")
                choose.append("P")
            elif check[1] == "Z":
                erg.append("L")
                choose.append("S")
        elif check[0] == "B":  # wenn paper
            if check[1] == "X":
                erg.append("L")
                choose.append("R")
            elif check[1] == "Y":
                erg.append("D")
                choose.append("P")
            elif check[1] == "Z":
                erg.append("W")
                choose.append("S")
        elif check[0] == "C":  # wenn schere
            if check[1] == "X":
                erg.append("W")
                choose.append("R")
            elif check[1] == "Y":
                erg.append("L")
                choose.append("P")
            elif check[1] == "Z":
                erg.append("D")
                choose.append("S")
        else:
            pass
    total = 0
    for i in erg:
        if i == "W":
            total += 6
        elif i == "D":
            total += 3

    for i in choose:
        if i == "R":
            total += 1
        elif i == "P":
            total += 2
        else:
            total += 3

    return total


print(solve())


def solve2():
    erg2 = []
    choose2 = []
    for i in range(len(inp)):
        check = tuple(inp[i])
        check = check[::2]
        if len(check) != 2:
            continue
        if check[0] == "A":  # wenn rock
            if check[1] == "X":
                erg2.append("L")
                choose2.append("S")
            elif check[1] == "Y":
                erg2.append("D")
                choose2.append("R")
            elif check[1] == "Z":
                erg2.append("W")
                choose2.append("P")
        elif check[0] == "B":  # wenn paper
            if check[1] == "X":
                erg2.append("L")
                choose2.append("R")
            elif check[1] == "Y":
                erg2.append("D")
                choose2.append("P")
            elif check[1] == "Z":
                erg2.append("W")
                choose2.append("S")
        elif check[0] == "C":  # wenn schere
            if check[1] == "X":
                erg2.append("L")
                choose2.append("P")
            elif check[1] == "Y":
                erg2.append("D")
                choose2.append("S")
            elif check[1] == "Z":
                erg2.append("W")
                choose2.append("R")
        else:
            pass
    total = 0
    for i in erg2:
        if i == "W":
            total += 6
        elif i == "D":
            total += 3

    for i in choose2:
        if i == "R":
            total += 1
        elif i == "P":
            total += 2
        else:
            total += 3

    return total


print(solve2())
