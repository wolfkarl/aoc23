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

    def blocks_from_end(self):
        block_start = None
        block_length = None
        block_content = None

        for i, c in reversed(list(enumerate(self.content))):
            # print(block_content)
            if block_start:
                if c == block_content:
                    block_length += 1
                    block_start = i
                    continue
                else:
                    yield(block_start, block_length)
                    block_start = None
                    block_length = None
                    block_content = None

            if c != ".":
                block_content = c
                block_start = i
                block_length = 1

    def leftmost_space_for(self, size: int, leftof: int):
        start, length = None, None
        for i, c in enumerate(self.content):
            if start:
                if c == ".":
                    length += 1
                elif length >= size:
                    return start
                else:
                    start = None
                    length = None
                    
            else:
                if i >= leftof:
                        return
                if c == ".":
                    start = i
                    length = 1


    def swap(self, a: int, b: int):
        self.content[a], self.content[b] = self.content[b], self.content[a]

    def swap_block(self, a, b, length):
        for i in range(length):
            self.swap(a+i, b+i)

    def expand(self,s):
        expanded = []
        for i, c in enumerate(s):
            if i % 2 == 0:
                content = str(i//2)
            else:
                content = "."

            expanded += [content] * int(c)

        return expanded

    def compact(self):
        datagen = self.data_from_end()
        for a in self.spaces():
            d = next(datagen)
            if d <= a:
                break
            self.swap(a, d)
            # print(self)

    def compact_blockwise(self):
        for blockstart, blocklength in self.blocks_from_end():
            spacestart = self.leftmost_space_for(blocklength, blockstart)
            if spacestart:
                self.swap_block(blockstart, spacestart, blocklength)

    def checksum(self):
        return sum([i*int(c) for i, c in enumerate(self.content) if c != "."])

    def __str__(self):
        return "|".join(self.content)

fs = Filesystem(line)
fs.compact()
print(fs)
print(fs.checksum())

fs2 = Filesystem(line)
fs2.compact_blockwise()
print(fs2)
print(fs2.checksum())