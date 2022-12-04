inp = open("testinput.txt").read().split("\n")

print(inp)


def convert(x, y):
    test1 = ""
    test2 = ""
    for i in range(int(x[0]) - 1):
        test1 += "."

    for i in range(int(x[0]),int(x[2])+1):
        test1 += str(i)

    for i in range(0,9 - len(test1)):
        test1 += "."

    for i in range(int(y[0])- 1):
        test2 += "."

    for i in range(int(y[0]),int(y[2])+1):
        test2 += str(i)

    for i in range(0,9 - len(test2)):
        test2 += "."

    zerg = []
    zerg.append(test1)
    zerg.append(test2)
    zerg.append(x)
    zerg.append(y)

    return zerg

def equal(x):
    print(x)
    sum = 0
    for i in x[0]:
        for e in range(len(x[1])):
            if i != ".":
                if i in x[1]:
                    sum += 1
                    if sum == len(x[0]):
                        c = True
                        print(c)
            break


def solve():
    for i in range(len(inp)):
        check = inp[i]
        check1 = check[:3]
        check2 = check[4:]
        equal(convert(check1, check2))

print(solve())
