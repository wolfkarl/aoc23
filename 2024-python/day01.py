from aocd import puzzle
import re


def parse_input(input):
    l1 = []
    l2 = []

    for line in input.split("\n"):
        matches = re.findall("\\d+", line)
        l1.append(int(matches[0]))
        l2.append(int(matches[1]))

    return l1, l2


def part1(l1, l2):


    pairs = list(zip(sorted(l1), sorted(l2)))

    sum = 0
    for e1, e2 in pairs:
        sum += abs(e1 - e2)

    return sum


def part2(l1, l2):
    total_score = 0
    for e1 in l1:
        # how often is e1 in l2
        score = e1 * l2.count(e1)
        total_score += score

    return total_score

l1, l2 = parse_input(puzzle.input_data)

print(part1(l1, l2))
print(part2(l1, l2))


