inp = open("input.txt").read().split("\n")

print(inp)


def createdic():
    alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
             "v",
             "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
             "R",
             "S", "T", "U", "V", "W", "X", "Y", "Z"]
    lis = []
    count = 0
    for i in alpha:
        count += 1
        lis.append((i, count))
    dic = dict(lis)
    return dic


def solve():
    erg = []
    for i in inp:
        checkfirst = i[:int((len(i)) / 2)]
        checklast = i[int((len(i)) / 2):int(len(i))]
        for e in range(len(checkfirst)):
            for w in range(len(checklast)):
                ergl = len(erg)
                if checkfirst[e] == checklast[w]:
                    erg.append(checkfirst[e])
                    break

            if len(erg) != ergl:
                break
    return add(erg, createdic())


def add(erg, dic):
    total = 0
    for i in erg:
        total += dic[i]

    return total


print("Aufgabe 1: " + str(solve()))


def solve2():
    erg = []
    inp2 = inp
    schleif = True
    while schleif:

        check = inp2[0]
        checknext = inp[1]
        checklast = inp[2]
        for e in range(len(check)):
            check1 = False
            check2 = False
            if not check1:
                for w in range(len(checknext)):
                    if check[e] == checknext[w]:
                        check1 = True
                        break
            if not check2 and check1:
                for w in range(len(checklast)):
                    if check[e] == checklast[w]:
                        check2 = True
                        break
            if check1 and check2:
                erg.append(check[e])
                break
        for i in range(3):
            if len(inp2) > 3:
                inp2.remove(inp2[0])
            elif len(inp2) < 3:
                schleif = False
            else:
                schleif = False
    return add(erg, createdic())


print("Aufgabe 2: " + str(solve2()))
