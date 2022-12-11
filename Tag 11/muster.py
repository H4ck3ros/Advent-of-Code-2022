
inp = open("input.txt").read().split("\n")



class Monkey:
    def __init__(self, starting_items, operation, tests, worryred):
        self.items = starting_items[::-1]
        self.op = operation
        self.tests = tests
        self.inspection_count = 0
        self.worryred = worryred

    def inspect(self):
        self.inspection_count += 1
        worry = self.items.pop()
        worry = self.operate(worry)
        worry = int(eval(self.worryred.replace("x", str(worry))))
        if worry % self.tests[0] == 0:
            return self.tests[1], worry
        else:
            return self.tests[2], worry

    def catch(self, item):
        self.items.insert(0, item)

    def operate(self, value):
        return eval(self.op.replace("x", str(value)))

    def __repr__(self):
        return str(self.items[::-1]) + " " + self.op + " " + str(self.tests) + " inspections: " + str(
            self.inspection_count)


def part1(inp):
    monkeys = []
    for e in inp:
        f = e.split("\n")
        items = [int(x) for x in f[1].split(": ")[1].split(", ")]
        operation = f[2].split("= ")[1].replace("old", "x")
        tests = [int(f[3].split(" ")[-1]), int(f[4].split(" ")[-1]), int(f[5].split(" ")[-1])]
        monkeys.append(Monkey(items, operation, tests, "x / 3"))

    for i in range(20):
        for m in monkeys:
            for j in range(len(m.items)):
                res = m.inspect()
                monkeys[res[0]].catch(res[1])
    res = sorted([m.inspection_count for m in monkeys])[::-1][:2]
    return res[0] * res[1]


def part2(inp):
    monkeys = []
    for e in inp:
        f = e.split("\n")
        items = [int(x) for x in f[1].split(": ")[1].split(", ")]
        operation = f[2].split("= ")[1].replace("old", "x")
        tests = [int(f[3].split(" ")[-1]), int(f[4].split(" ")[-1]), int(f[5].split(" ")[-1])]
        monkeys.append(
            Monkey(items, operation, tests,
                   ""))

    vals = [x.tests[0] for x in monkeys]
    kgv = 1
    for e in vals:
        kgv *= e

    for m in monkeys:
        m.worryred = "x % " + str(kgv)

    for i in range(10000):
        for m in monkeys:
            for j in range(len(m.items)):
                res = m.inspect()
                monkeys[res[0]].catch(res[1])
    res = sorted([m.inspection_count for m in monkeys])[::-1][:2]
    return res[0] * res[1]

part1(inp)