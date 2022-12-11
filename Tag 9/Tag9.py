inp = open("input.txt").read().split("\n")

class Knot:
    def __init__(self, pos, id):
        self.history = {pos}
        self._pos = pos
        self.id = id

    def getpos(self):
        return self._pos

    def setpos(self, pos):
        self._pos = pos
        self.history.add(pos)

    pos = property(getpos, setpos)


def updateT(t, h):
    moves = {(2, 0): (1, 0), (-2, 0): (-1, 0), (0, 2): (0, 1), (0, -2): (0, -1), (2, -1): (1, -1), (2, 1): (1, 1),
             (-2, -1): (-1, -1), (-2, 1): (-1, 1), (-1, 2): (-1, 1), (1, 2): (1, 1), (-1, -2): (-1, -1),
             (1, -2): (1, -1), (2, 2): (1, 1), (-2, -2): (-1, -1), (-2, 2): (-1, 1), (2, -2): (1, -1)}
    offset = tuple(map(lambda i, j: i - j, h.pos, t.pos))

    if offset in moves:
        t.pos = (t.pos[0] + moves[offset][0], t.pos[1] + moves[offset][1])


def part1(inp):
    h = Knot((0, 0), "H")
    t = Knot((0, 0), "T")

    moves = {"L": (-1, 0), "R": (1, 0), "U": (0, -1), "D": (0, 1)}

    for e in inp:
        e = e.split(" ")
        for i in range(int(e[1])):
            h.pos = tuple(map(lambda j, k: j + k, h.pos, moves[e[0]]))
            updateT(t, h)
    return len(t.history)


def part2(inp):
    h = Knot((0, 0), "H")
    tails = [Knot((0, 0), i) for i in range(1, 9)]
    tails.append(Knot((0, 0), "T"))

    moves = {"L": (-1, 0), "R": (1, 0), "U": (0, -1), "D": (0, 1)}

    for e in inp:
        e = e.split(" ")
        for i in range(int(e[1])):
            h.pos = tuple(map(lambda j, k: j + k, h.pos, moves[e[0]]))
            prev = h
            for f in tails:
                updateT(f, prev)
                prev = f
    return len(tails[-1].history)

print(part1(inp))
print(part2(inp))