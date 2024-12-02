from aocd import puzzle

lines =  puzzle.input_data.split("\n")

def is_safe(numbers: list[int]):
    if len(numbers) < 3:
        return True
    
    diff1 = numbers[0] - numbers[1]
    diff2 = numbers[1] - numbers[2]

    if (diff1 > 0) != (diff2 > 0):
        return False
    
    for diff in [diff1, diff2]:
        if abs(diff) < 1 or abs(diff) > 3:
            return False
        
    return is_safe(numbers[1:])

def is_safe_dampened(numbers: list[int], dampened=False):
    if len(numbers) < 3:
        return True
    
    safe = True
    
    diff1 = numbers[0] - numbers[1]
    diff2 = numbers[1] - numbers[2]

    if (diff1 > 0) != (diff2 > 0):
        safe = False
    
    for diff in [diff1, diff2]:
        if abs(diff) < 1 or abs(diff) > 3:
            safe = False

    if not safe:
        if dampened:
            return False
        else:
            return (
                is_safe_dampened([numbers[0], numbers[1], *numbers[3:]], True) or
                is_safe_dampened([numbers[1], numbers[2], *numbers[3:]], True) or
                is_safe_dampened([numbers[0], numbers[2], *numbers[3:]], True) 
                )
        
    return is_safe_dampened(numbers[1:], dampened)

def parse_line(line):
    return [int(num) for num in line.split(" ")]


def safe_icon(s):
    if s:
        return "✅"
    else:
        return "❌"

rows = [parse_line(line) for line in lines]

# part 1
safe = [is_safe(row) for row in rows]
num_safe = safe.count(True)
print(num_safe)

# part 2
almost_safe =  [is_safe_dampened(row, False) for row in rows]
print(almost_safe)
print(almost_safe.count(True))