from pathlib import Path
from functools import reduce


def read_input():
    return [int(x) for x in Path("input.txt").read_text().splitlines()]


def part1(numbers):
    pairs = []
    for i, n in enumerate(numbers):
        for m in numbers[i:]:
            if n + m == 2020:
                pairs.append((n, m))
    assert len(pairs) == 1
    print(reduce(lambda x, y: x * y, pairs[0]))


def part2(numbers):
    tuples = []
    for i, n in enumerate(numbers):
        for j, m in enumerate(numbers[i:]):
            for o in numbers[j:]:
                if n + m + o == 2020:
                    tuples.append((n, m, o))

    assert len(tuples) == 1
    print(reduce(lambda x, y: x * y, tuples[0]))


numbers = read_input()
part1(numbers)
part2(numbers)
