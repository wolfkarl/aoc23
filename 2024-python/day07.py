from aocd import puzzle


def working_results(line, allow_concat):
    print(line)
    result, elements = line.split(": ")
    result = int(result)
    elements = [int(e) for e in elements.split(" ")]
    num_options =  try_operands(elements, result, allow_concat)
    if num_options > 0:
        return result
    else:
        return 0
    
def concat(a, b) -> int:
    return int(str(a) + str(b))


def try_operands(elements, result, allow_concat=False) -> int:

    if len(elements) < 2:
        if elements[0] == result:
            return 1
        else:
            return 0

    e1 = elements.pop(0)
    e2 = elements.pop(0)

    if e1 > result:
        return 0

    num_options = (
        try_operands([e1 + e2] + elements, result, allow_concat) + 
        try_operands([e1 * e2] + elements, result, allow_concat)
    )

    if allow_concat:
        num_options += try_operands([concat(e1, e2)] + elements, result, allow_concat)

    return num_options

lines = puzzle.examples[0].input_data
lines = puzzle.input_data

part1 = sum([working_results(line, allow_concat=False) for line in lines.split("\n")])
print(part1)

part2 = sum([working_results(line, allow_concat=True) for line in lines.split("\n")])
print(part2)
