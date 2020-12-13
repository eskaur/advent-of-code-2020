from pathlib import Path
from dataclasses import dataclass
from operator import xor
import re


input_pattern = re.compile(r"(?P<i>\d+)-(?P<j>\d+) (?P<letter>[a-z]): (?P<pw>\w+)")


@dataclass
class Entry:
    letter: str
    i: int
    j: int
    pw: str

    def __post_init__(self):
        self.i = int(self.i)
        self.j = int(self.j)


def parse_entry(line):
    match = input_pattern.match(line)
    return Entry(**match.groupdict())


def read_input():
    return [parse_entry(line) for line in Path("input.txt").read_text().splitlines()]


def is_valid_part1(entry):
    count = entry.pw.count(entry.letter)
    return count >= entry.i and count <= entry.j


def is_valid_part2(entry):
    first = entry.pw[entry.i - 1] == entry.letter
    second = entry.pw[entry.j - 1] == entry.letter
    return xor(first, second)


def part1(entries):
    valid = map(lambda x: is_valid_part1(x), entries)
    print(sum(valid))


def part2(entries):
    valid = map(lambda x: is_valid_part2(x), entries)
    print(sum(valid))


entries = read_input()
part1(entries)
part2(entries)
