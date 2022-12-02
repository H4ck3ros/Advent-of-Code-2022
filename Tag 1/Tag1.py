inp = open("input.txt").read().split("\n")

def solve():
    most = []
    last = []
    add = 0
    for i in inp:
        if i != '':
            add += int(i)
        else:
            most.append(add)
            add = 0
    for i in range(3):
        last.append(max(most))
        most.remove(max(most))

    return str(max(most)), str(sum(last))


print(" ".join(solve()))
