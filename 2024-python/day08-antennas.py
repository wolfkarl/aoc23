from aocd import puzzle
import progressbar
import copy
from collections import defaultdict

class Grid:

    EMPTY = "."

    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.rows = [[self.EMPTY for _ in range(width)] for _ in range(height)]

    @classmethod
    def from_string(cls, rows):
        g = Grid(0,0)
        g.rows = [list(row) for row in rows.split("\n")]
        g.width = len(g.rows[0])
        g.height = len(g.rows)
        return g
    
    def set(self, pos, s):
        i,j = pos
        if pos in self:
            self.rows[j][i] = s

    def get(self, pos):
        i,j = pos
        if pos in self:
            return self.rows[j][i] 
        else: 
            return self.EMPTY

    def count(self, s):
        return sum([row.count(s) for row in self.rows])
    
    def make_overlay(self):
        return Grid(self.width, self.height)

    def __str__(self):
        return "\n".join(["".join(row) for row in self.rows])
    
    def __contains__(self, coord):
        (x,y) = coord
        return x in range(self.width) and y in range(self.height)
    
    def find(self, char):
        for j, row in enumerate(self.rows):
            if char in row:
                return (row.index(char), j)
            
        raise ValueError("Not found")
    
    def cells(self):
        for j, row in enumerate(self.rows):
            for i, cell in enumerate(row):
                yield(i,j,cell)


    


lines = puzzle.examples[0].input_data
lines = puzzle.input_data

g = Grid.from_string(lines)


antennas = defaultdict(list)

for (i,j,cell) in g.cells():
    if not cell == ".":
        antennas[cell].append((i,j))

print(antennas)

def nodes_simple(antennas, g):
    nodes = g.make_overlay()

    for (antenna, locations) in antennas.items():
        locations = locations.copy()
        while len(locations) > 1:
            main_i, main_j = locations.pop(0)
            for other_i, other_j in locations:
                diff_i, diff_j = main_i - other_i, main_j - other_j
                nodes.set((main_i + diff_i, main_j + diff_j), "#")
                nodes.set((other_i - diff_i, other_j - diff_j), "#")

    return nodes

def nodes_multiple(antennas, g):
    nodes = g.make_overlay()

    for (antenna, locations) in antennas.items():
        locations = locations.copy()
        while len(locations) > 1:
            main_i, main_j = locations.pop(0)
            for other_i, other_j in locations:
                diff_i, diff_j = main_i - other_i, main_j - other_j

                m = 1
                while True:
                    m_pos = (main_i + diff_i * m, main_j + diff_j * m)
                    print(m_pos)
                    if not m_pos in g:
                        break
                    nodes.set(m_pos, "#")
                    m += 1

                m = 0
                while True:
                    m_pos = (main_i + diff_i * m, main_j + diff_j * m)
                    if not m_pos in g:
                        break
                    nodes.set(m_pos, "#")
                    m -= 1

            print(nodes)
            print()

    return nodes

print(nodes_simple(antennas, g).count("#"))
print(nodes_multiple(antennas, g).count("#"))

            

# print(g)