import re
import functools

from aocd import puzzle
print(puzzle.examples)
code = puzzle.examples[0].input_data
print(code)

def eval_muls(code):

    pattern = re.compile("mul\\((\\d+),(\\d+)\\)")
    matches = pattern.findall(code)

    def mul(tpl): 
        (a, b) = tpl
        return int(a) * int(b)

    products = map(mul, matches)
    return sum(products)

def allowed_code_parts(code):
    # not bothering with multline regex, just removing line endings
    code = "do()" + code.replace("\n", "") + "don't()"
    pattern = re.compile("do\\(\\).*?don't\\(\\)")
    matches = pattern.findall(code)
    print(len(matches))
    return matches

def eval_allowed(code):
    sums = [eval_muls(codepart) for codepart in allowed_code_parts(code)]
    print(sums)
    return sum(sums)


example2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

assert(eval_muls(puzzle.examples[0].input_data) == 161)

print(eval_muls(puzzle.input_data))


assert(eval_allowed(example2) == 48)

assert(eval_allowed("mul(1,3)do()mul(1,10)") == 13)

print(eval_allowed(puzzle.input_data))