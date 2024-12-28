from collections import defaultdict
from aocd import puzzle
from progressbar import progressbar

lines = puzzle.input_data
start_numbers = [int(line) for line in lines.split("\n")]

# print(start_numbers)

"""
    Calculate the result of multiplying the secret number by 64. Then, mix this result into the secret number. Finally, prune the secret number.
    Calculate the result of dividing the secret number by 32. Round the result down to the nearest integer. Then, mix this result into the secret number. Finally, prune the secret number.
    Calculate the result of multiplying the secret number by 2048. Then, mix this result into the secret number. Finally, prune the secret number.
"""

def generate(s):
    s = prune(mix(s, s*64))
    s = prune(mix(s, s // 32))
    s = prune(mix(s, s * 2048))
    return s

def mix(n, s):
    return n ^ s

def prune(n):
    return n % 16777216

def gen_x(s, x):
    for i in range(x):
        s = generate(s)

    return s


STEPS = 2000


def get_sequences(start_number):
    last_four = []
    s = start_number
    for i in range(STEPS):
        s1 = generate(s)
        change = (s1 % 10) - (s % 10)
        last_four.append(change)
        last_four = last_four[-4:]
        if len(last_four) == 4:
            yield last_four
        s = s1
        # print(last_four)

def buy_sequence(start_number, sequence):
    s = start_number
    last_four = []
    for i in range(STEPS):
        s1 = generate(s)
        change = (s1 % 10) - (s % 10)
        last_four.append(change)
        last_four = last_four[-4:]
        # print(last_four)

        if last_four == sequence:
            return s1 % 10
        
        s = s1

    return 0

def buy_sequence_all(sequence):
    global start_numbers
    prices = [buy_sequence(sn, sequence) for sn in start_numbers]
    return sum(prices)


assert(gen_x(1, 2000) == 8685429)
assert(gen_x(10, 2000) == 4700978)

# Part 1
secrets_sum = 0
for start_number in progressbar(start_numbers):
    secrets_sum += gen_x(start_number, 2000)
print(secrets_sum)

seq_prices = defaultdict(int)

def add_sequence(start_number):
    global seq_prices
    seqs_done = set()
    last_four = []
    s = start_number
    for i in range(STEPS):
        s1 = generate(s)
        change = (s1 % 10) - (s % 10)
        last_four.append(change)
        last_four = last_four[-4:]
        skey = str(last_four)
        if len(last_four) == 4 and skey not in seqs_done:
            seq_prices[skey] += s1 % 10
            seqs_done.add(skey)
        s = s1
        # print(last_four)

[add_sequence(sn) for sn in progressbar(start_numbers)]

max_price = max(seq_prices, key=seq_prices.get)
# print(seq_prices)
print(max_price)
print(seq_prices[max_price])
# print(seq_prices.index(max_price))
