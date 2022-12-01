inp = open("input.txt").read().split("\n")

most = []
add = 0

for i in inp:
    if i != '':
        add += int(i)
    else:
        most.append(add)
        add = 0

last = []

for i in range(3):
    last.append(max(most))
    most.remove(max(most))

print(sum(last))
