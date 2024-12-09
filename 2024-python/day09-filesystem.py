from aocd import puzzle
from copy import copy

line = puzzle.examples[0].input_data
line = puzzle.input_data


class Filesystem:

    def __init__(self, s):
        self.content = list(self.expand(s))

    def spaces(self):
        for i, c in enumerate(self.content):
            if c == ".":
                yield i

    def data_from_end(self):
        for i, c in reversed(list(enumerate(self.content))):
            if c != ".":
                yield i

    def swap(self, a: int, b: int):
        self.content[a], self.content[b] = self.content[b], self.content[a]

    def expand(self,s):
        expanded = ""
        for i, c in enumerate(s):
            if i % 2 == 0:
                content = str(i//2)
            else:
                content = "."

            expanded += content * int(c)

        return expanded

    def compact(self):
        datagen = self.data_from_end()
        for a in self.spaces():
            d = next(datagen)
            if d <= a:
                break
            self.swap(a, d)
            # print(self)

    def checksum(self):
        return sum([i*int(c) for i, c in enumerate(self.content) if c != "."])

    def __str__(self):
        return "".join(self.content)

fs = Filesystem(line)
fs.compact()
print(fs)
print(fs.checksum())