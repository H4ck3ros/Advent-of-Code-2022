inp = open("testinput.txt").read().split("\n")

class Tree:
    def __init__(self, item):
        self.parent = None
        self.children = []
        self.item = item
        self.size = 0


def solve(inp):
    tree = Tree("/")
    root = tree
    for i in inp[1:]:
        s = i.split(" ")
        if i[0] == "$":
            if s[1] == "cd":
                if s[-1] != "..":
                    p = 0
                    for e in tree.children:
                        if e.item[0] == s[-1]:
                            tree = e
                            p = e
                            break

                else:
                    tree = tree.parent
            continue

        if s[0] == "dir":
            tree1 = Tree((s[1], s[0]))
            tree.children.append(tree1)
            tree1.parent = tree
            continue
        if i[0] != "$":
            tree2 = Tree((s[1], s[0]))
            tree.children.append(tree2)
            tree2.parent = tree
            continue
    return root


def print_tree(depth, tree):
    if tree.item[-1] == "dir":
        print(2 * depth * " " + "- " + tree.item[0] + " (dir)")
    else:
        print(2 * depth * " " + "- " + tree.item[0] + " (file, size=" + tree.item[-1] + ")")
    for e in tree.children:
        print_tree(depth + 1, e)


def get_size(tree):
    for e in tree.children:
        if e.item[-1] != "dir":
            tree.size += int(e.item[-1])
        else:
            tree.size += get_size(e)
    return tree.size


def calculate(tree):
    s = 0
    for e in tree.children:
        s += calculate(e)
    if tree.item[-1] == "dir" and tree.size <= 100000:
        return tree.size + s
    return s


def complete_solve(inp):
    tree = solve(inp)
    #print_tree(0, tree)
    get_size(tree)
    return print("Aufgabe 1: " + str(calculate(tree)))


print(complete_solve(inp))


def get_directories(tree):
    tmp = []
    print(tree.item, tree)
    print(tree.children)
    for e in tree.children:
        print("hello")
        tmp.extend(get_directories(e))
    if tree.item[-1] == "dir":
        return tmp.append(tree)
    return tmp


def part2(inp):
    tree = solve(inp)
    get_size(tree)
    directories = sorted(get_directories(tree), key=lambda x: x.size)
    for e in directories:
        if (70000000 - tree.size) + e.size >= 30000000:
            return e.size

print(part2(inp))