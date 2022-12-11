inp = open("testinput.txt").read().split("\n")


def monkeys(inp):
    mlist = []
    for i in inp:
        i = str(i).split(" ")
        if len(i) == 2:
            mlist.append(i)
    start_items = []
    for i in inp:
        i = str(i).split(" ")
        if len(i) > 2:
            if i[3] == "items:":
                start_items.append(i[4:])
    opp = []
    for i in inp:
        i = str(i).split(" ")
        if len(i) > 2:
            if i[3] == "new":
                opp.append(i[5:])
    test = []
    for i in inp:
        i = str(i).split(" ")
        if len(i) > 2:
            if i[2] == "Test:":
                test.append(i[5:])
    do = []
    for i in inp:
        i = str(i).split(" ")
        if len(i) > 2:
            if i[4] == "If":
                do.append(i[-1])
    help = do
    do_final = []
    while True:
        a = help.pop(0)
        b = help.pop(0)
        do_final.append((a, b))
        if len(help) == 0:
            break
    monkey_list = {}
    count = 0
    for i in mlist:
        monkey_list[count] = [start_items[count], opp[count], test[count], do_final[count]]
        count += 1
    return monkey_list


def solve():
    mlist = monkeys(inp)
    print(mlist)

    for key in mlist.items():
        print(key)
        for e in range(len(key[1][0])):
            check = key[1][0][e]
            check1 = ""
            for i in check:
                if i != ",":
                    check1 += i
            check1 = int(check1)
            final_check = new_value(check1, key)
            final_check = int(final_check / 3)
            if final_check % int(key[1][2][0]) == 0:
                #wrif zu afffe von k[1][3][0]
                pass
            else:
                mlist.items()
                #wirf zu affe von
            print(final_check)


def new_value(x, lis): # funktoniert
    operation = lis[1][1]
    print(operation)
    if operation[1] == "*":
        if operation[2] != operation[0]:
            return x * int(operation[2])
        else:
            return x * x
    else:
        if operation[2] != operation[0]:
            return x + int(operation[2])
        else:
            return x + x


print(solve())
