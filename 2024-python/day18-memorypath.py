from collections import defaultdict
from aocd import puzzle
from progressbar import progressbar


# A common example of a graph-based pathfinding algorithm is Dijkstra's algorithm. This algorithm begins with a start node and an "open set" of candidate nodes. At each step, the node in the open set with the lowest distance from the start is examined. The node is marked "closed", and all nodes adjacent to it are added to the open set if they have not already been examined. This process repeats until a path to the destination has been found. Since the lowest distance nodes are examined first, the first time the destination is found, the path to it will be the shortest path.

class Space:

    def __init__(self, lines, size):
        self.corruptions = [[int(i) for i in line.split(",")] for line in lines]
        self.size = size


    def find_shortest_path(self):
        start = (0,0)
        goal = (self.size-1, self.size-1)

        self.open = defaultdict(set) # distance -> x,y
        self.open[0] = [start]
        self.closed = set() # x,y

        # self.print()


        MAX = 100_000
        while MAX > 0:
            MAX -= 1

            # print(self.open, self.closed)
            try:
                distances = [key for key in self.open.keys() if len(self.open[key]) > 0]
                shortest_distance = sorted(distances)[0]
                ix, iy = self.open[shortest_distance].pop()

                if (ix, iy) == goal:
                    return shortest_distance

                else:

                    for nb in self.get_neighbours(ix, iy):
                        self.open[shortest_distance+1].add(nb)

                    self.closed.add((ix, iy))
            except IndexError:
                self.print()
                return -1

    def print(self):
        for i in range(self.size):
            for j in range(self.size):
                if(i,j) in self.closed:
                    c = "0"
                elif [i,j] in self.corruptions:
                    c = "#"
                else:
                    c = "."
                print(c, end="")
            print("\n")
        print("\n\n")

    def get_neighbours(self, x,y):
        nbs = []
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = (x+dx, y+dy)

            if nx not in range(self.size) or ny not in range(self.size):
                continue
            if (nx, ny) in self.closed:
                continue
            if [nx, ny] in self.corruptions:
                continue

            nbs.append((nx, ny))
        return nbs

# corruption_lines = puzzle.examples[0].input_data.split("\n")
# size = 7

corruption_lines = puzzle.input_data.split("\n")
size = 70 + 1

for i in progressbar(range(len(corruption_lines))):
    # brute force approach, we could also store the actual shortest path and
    # skip ahead when the new byte is not on the path
    sp = Space(corruption_lines[:i+1], size)
    path = sp.find_shortest_path()
    if path < 0:
        print(i, corruption_lines[i], path)
        break