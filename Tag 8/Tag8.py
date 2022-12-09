inp = open("input.txt").read().split("\n")


class Tree:
    def __init__(self, n):
        self.n = n
        self.seen = False
        self.scenic = 0


def part1(inp):
    forest = []
    for e in inp:
        forest.append([Tree(int(x)) for x in list(e)])

    # Check if tree is seen in a left-to-right sweep
    for j in range(len(forest[0])):
        prev = -1
        for k in range(len(forest)):
            if forest[k][j].n > prev:
                forest[k][j].seen = True
            prev = max(prev, forest[k][j].n)

    # Check if tree is seen in a right-to-left sweep
    for j in range(len(forest[0])):
        prev = -1
        for k in range(len(forest)):
            if forest[len(forest) - 1 - k][j].n > prev:
                forest[len(forest) - 1 - k][j].seen = True
            prev = max(prev, forest[len(forest) - 1 - k][j].n)

    # Check if tree is seen in a top-to-bottom sweep
    for j in range(len(forest)):
        prev = -1
        for k in range(len(forest[j])):
            if forest[j][k].n > prev:
                forest[j][k].seen = True
            prev = max(prev, forest[j][k].n)

    # Check if tree is seen in a bottom-to-top sweep
    for j in range(len(forest)):
        prev = -1
        for k in range(len(forest[j])):
            if forest[j][len(forest[j]) - 1 - k].n > prev:
                forest[j][len(forest[j]) - 1 - k].seen = True
            prev = max(prev, forest[j][len(forest[j]) - 1 - k].n)

    count = 0
    for i in range(len(forest)):
        for j in range(len(forest[i])):
            if forest[i][j].seen:
                count += 1
    return count


def part2(inp):
    forest = []
    for e in inp:
        forest.append([Tree(int(x)) for x in list(e)])

    for x in range(len(forest)):
        for y in range(len(forest[x])):
            forest[x][y].scenic = 1
            for e in [(1, len(forest[x]), 1), (-1, -1, -1)]:
                tmp = 0
                for i in range(y + e[0], e[1], e[2]):
                    if forest[x][i].n < forest[x][y].n:
                        tmp += 1
                    if forest[x][i].n >= forest[x][y].n:
                        tmp += 1
                        break
                forest[x][y].scenic *= tmp

            for e in [(1, len(forest[y]), 1), (-1, -1, -1)]:
                tmp = 0
                for i in range(x + e[0], e[1], e[2]):
                    if forest[i][y].n < forest[x][y].n:
                        tmp += 1
                    if forest[i][y].n >= forest[x][y].n:
                        tmp += 1
                        break
                forest[x][y].scenic *= tmp
    return max(tree.scenic for row in forest for tree in row)



res = part1(inp)

print("Part 1:")
print(res)

print("Part 2:")
res = part2(inp)
print(res)