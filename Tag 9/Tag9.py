inp = open("testinput.txt").read().split("\n")

print(inp)
erg = {}

last = ()
print(last)
direction = ""

start = (0, 0)
for i in inp:
    for e in range(int(i[-1])):

        if i[0] == "R":
            start = (start[0] + 1, start[1])
        if i[0] == "L":
            start = (start[0] - 1, start[1])
        if i[0] == "U":
            start = (start[0], start[1] + 1)
        if i[0] == "D":
            start = (start[0], start[1] - 1)

        last = start
        print("last: " + str(last))

    print(last)
