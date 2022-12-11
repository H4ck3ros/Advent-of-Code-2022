inp = open("testinput.txt").read().split("\n")


def solve(inp):
    x = 1
    erg = []
    cycle = 0
    for i in inp:
        i = i.split(" ")
        if len(i) == 1:
            cycle += 1
            if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
                erg.append(x * cycle)
        else:
            for e in range(2):
                cycle += 1
                if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
                    erg.append(x * cycle)
                if e == 1:
                    x += int(i[1])
    print("x: " + str(x), "cycle: " + str(cycle), "erg: " + str(sum(erg)))
    return ""


#print(solve(inp))


def solve2(inp):
    erg = ""
    cycle = 0
    position = 0
    last_reg = "###....................................."
    for i in inp:
        i = i.split(" ")
        register = last_reg
        if len(i) == 1:
            if cycle == 40 or cycle == 80 or cycle == 120 or cycle == 160 or cycle == 200 or cycle == 240:
                print(erg)
                position = 0
                erg = ""
            cycle += 1
            erg = erg + register[position]
            position += 1
        else:
            for e in range(2):
                if cycle == 40 or cycle == 80 or cycle == 120 or cycle == 160 or cycle == 200 or cycle == 240:
                    print(erg)
                    position = 0
                    erg = ""
                cycle += 1
                erg = erg + register[position]
                position += 1
            last_reg = sprite(i[-1], last_reg)
        print(register, position, cycle, last_reg, i[-1])
    print(erg)

    return ""


def sprite(x, last_reg):
    y = int(x)
    register = last_reg
    check = False
    if int(x) < 0:
        y *= -1
        check = True
    for i in range(y):
        if check:
            register = register[1:]
        else:
            register = register[:len(register) - 1]

    for e in range(y):
        if check:
            register = register + "."
        else:
            register = "." + register
    return register

print(solve2(inp))
