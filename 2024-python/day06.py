from aocd import puzzle
import progressbar
import copy

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

class Guard:

    DIRECTIONS = {
        "^": (0, -1),
        ">": (1,0),
        "v": (0, 1),
        "<": (-1, 0),
    }

    OBSTACLE = "#"

    def __init__(self, grid: Grid) -> None:
        self.grid = grid
        self.overlay = self.grid.make_overlay()
        self.direction = "^"
        self.starting_position = self.grid.find(self.direction)
        self.position = self.starting_position

    def next_position(self) -> tuple[int,int]:
        x, y = self.DIRECTIONS[self.direction]
        i, j = self.position
        new_position = (i+x, j+y)
        return new_position

    def next_direction(self) -> tuple[int, int]:
       symbols = list(self.DIRECTIONS.keys())
       idx = symbols.index(self.direction)
       new_idx = symbols[(idx+1) % len(symbols)]
       return new_idx

    def patrol(self):

        # track all fields for all directions. if we walk the same field again in the
        # same direction, we've found a loop (or so I hope)

        direction_overlays = {key: self.grid.make_overlay() for key in self.DIRECTIONS.keys()}
        loop = False

        while(self.position in self.grid):

            self.grid.set(self.position, Grid.EMPTY)
            self.overlay.set(self.position, "X")
            newpos = self.next_position()

            if self.grid.get(newpos) == self.OBSTACLE:
                self.direction = self.next_direction()
            else:
                self.position = self.next_position()

            self.grid.set(self.position, self.direction)

            if direction_overlays[self.direction].get(self.position) == "X":
                loop = True
                break
            else:
                direction_overlays[self.direction].set(self.position, "X")

        return loop

            # print(self.grid)
        

lines = puzzle.input_data
# lines = puzzle.examples[0].input_data


# part 1

ig = Grid.from_string(lines)
guard1 = Guard(ig)

print(guard1.patrol())
# print(guard.overlay)
print(guard1.overlay.count("X"))


# part 2

ig = Grid.from_string(lines)

loops = 0

for j in progressbar.progressbar(range(ig.height)):
    for i in range(ig.width):
        if ig.get((i,j)) == "." and guard1.overlay.get((i,j)) == "X":
            igi = copy.deepcopy(ig)
            igi.set((i,j), "#")
            guard = Guard(igi)
            loop = guard.patrol()
            if loop:
                loops += 1

print(loops)


        