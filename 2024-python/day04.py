import re
from aocd import puzzle


class Grid:

    def __init__(self, rows):
        self.__rows = [list(row) for row in rows]
        self.height = len(rows)
        self.width = len(rows[0])
        assert all([len(row) == self.width] for row in self.__rows)

    def print(self):
        [print(row) for row in self.rows()]

    def rows(self):
        return self.__rows

    def row(self, i):
        return self.rows()[i]

    def cols(self):
        return [self.col(j) for j in range(self.width)]

    def col(self, j):
        return [row[j] for row in self.rows()]

    def cell(self, i, j):
        return self.__rows[i][j]

    def diagonal(self, i, j, x):
        diag = []
        while i < self.height and j >= 0 and j < self.width:
            diag.append(self.cell(i, j))
            i += 1
            j += x

        return diag

    def diagonals(self):
        diags = []

        # left to right, top row then starting on the side
        for j in range(0, self.width):
            diags.append(self.diagonal(0, j, 1))

        for i in range(1, self.height):
            diags.append(self.diagonal(i, 0, 1))

        # right to left
        for j in range(0, self.width):
            diags.append(self.diagonal(0, j, -1))

        for i in range(1, self.height):
            diags.append(self.diagonal(i, self.width - 1, -1))

        return diags

        # for i in range(1, grid.height)

    def blocks(self, w, h):
        blocks = []
        for i in range(self.height + 1 - h):
            for j in range(self.width + 1 - w):
                blocks.append(self.block(i, w, j, h))

        return blocks

    def block(self, x, w, y, h):
        block = []
        for i in range(x, x + h):
            for j in range(y, y + w):
                block += self.cell(i, j)

        return block


grid = Grid(puzzle.input_data.split("\n"))

# ex2 = """.M.S......
# ..A..MSMS.
# .M.S.MAA..
# ..A.ASMSM.
# .M.S.M....
# ..........
# S.S.S.S.S.
# .A.A.A.A..
# M.M.M.M.M.
# .........."""

# grid = Grid(ex2.split("\n"))


def find_xmas(haystack: list):
    text = "".join(haystack)
    xmas = re.compile("XMAS")
    matches = xmas.findall(text)
    return len(matches)


total_xmas = 0

for row in grid.rows():
    total_xmas += find_xmas(row)
    total_xmas += find_xmas(reversed(row))

for col in grid.cols():
    total_xmas += find_xmas(col)
    total_xmas += find_xmas(reversed(col))

for diag in grid.diagonals():
    total_xmas += find_xmas(diag)
    total_xmas += find_xmas(reversed(diag))

# grid.print()
print(total_xmas)


def block_is_xmas(block: list):
    inner = "".join([block[i] for i in [0, 2, 4, 6, 8]])
    return inner in ['MSAMS', 'MMASS', 'SMASM', 'SSAMM']

total_x = 0

for block in grid.blocks(3, 3):
    if block_is_xmas(block):
        total_x += 1


print(total_x)
