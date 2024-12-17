from aocd import puzzle 
from progressbar import progressbar
from collections import defaultdict

line = "125 17"
line = puzzle.input_data

stones = {int(s) : 1 for s in line.split(" ")}
print(stones)

def split_stone(stone):
    s = str(stone)
    sl = len(s)
    if sl % 2 == 0:
        slh = sl // 2
        return [int(s[slh:]), int(s[:slh])]
    else:
        return False

def blink(stones):
    blinked = defaultdict(int)
    for engraving, amount in stones.items():
        if engraving == 0:
            blinked[1] += amount
        elif split_stone(engraving):
            l, r = split_stone(engraving)
            blinked[l] += amount
            blinked[r] += amount
        else:
            blinked[engraving * 2024] += amount

    return blinked


for i in progressbar(range(75)):
    stones = blink(stones)
    # print(stones)
    print(sum(stones.values()))



## this is broken because of recursion depth

# class Stone:

#     def __init__(self, engraving: int, next = None):
#         self.engraving = engraving
#         self.next = next

#     def engraving_length(self):
#         return len(str(self.engraving))

#     def blink(self):
#         if self.engraving == 0:
#             self.engraving = 1
#         elif self.engraving_length() % 2 == 0:
#             new_stone = Stone(
#                 int(str(self.engraving)[:(self.engraving_length() // 2)]),
#                   next=self.next
#                 )
#             self.engraving = int(str(self.engraving)[(self.engraving_length() // 2):])
#             self.next = new_stone
#         else:
#             self.engraving *= 2024

#     def blink_through(self):
#         self.blink()
#         if self.next:
#             self.next.blink_through()

#     def count_through(self):
#         if self.next:
#             return self.next.count_through() + 1
#         else:
#             return 1

#     def following(self):
#         s = str(self.engraving) + " " 
#         if self.next:
#             s += self.next.following()
#         return s
    
# starts = reversed([int(s) for s in line.split(" ")])
# prev = None
# for eng in starts:
#     stone = Stone(eng, next=prev)
#     prev = stone

# print(stone.following())

# for i in range(25):
#     stone.blink_through()
#     # print(stone.following())
#     print(stone.count_through())