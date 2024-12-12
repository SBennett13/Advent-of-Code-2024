#!/usr/bin/env python3

from collections import namedtuple
import os

INPUT = os.path.join(os.path.abspath(os.path.dirname(__file__)), "input.txt")
EXAMPLE = os.path.join(os.path.abspath(os.path.dirname(__file__)), "example.txt")

Location = namedtuple("Location", ["r", "c"])
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3


def traverse(m: list[str], current_position: Location, tops: list = None):
    if tops is None:
        tops = []

    current_val = int(m[current_position.r][current_position.c])
    next_val = str(current_val + 1)
    if current_val == 9:
        tops.append(current_position)
        return

    for i in range(4):
        if i == UP:
            next_position = Location(current_position.r - 1, current_position.c)
        elif i == RIGHT:
            next_position = Location(current_position.r, current_position.c + 1)
        elif i == DOWN:
            next_position = Location(current_position.r + 1, current_position.c)
        elif i == LEFT:
            next_position = Location(current_position.r, current_position.c - 1)

        if (
            next_position.r >= len(m)
            or next_position.r < 0
            or next_position.c >= len(m[0])
            or next_position.c < 0
        ):
            continue
        if m[next_position.r][next_position.c] != next_val:
            continue

        traverse(m, next_position, tops)


def part1(m: list[str], trailheads: list[Location]):
    total = 0
    for head in trailheads:
        tops = []
        traverse(m, head, tops)
        total += len(set(tops))

    print(f"Part 1: {total}")


def part2(m: list[str], trailheads: list[Location]):
    total = 0
    for head in trailheads:
        tops = []
        traverse(m, head, tops)
        total += len(tops)

    print(f"Part 2: {total}")


def main():
    m = []
    trailheads = []
    with open(INPUT) as f:
        r = 0
        for line in f.readlines():
            m.append(line.strip())
            for i, score in enumerate(line.strip()):
                if score == "0":
                    trailheads.append(Location(r, i))

            r += 1

    part1(m, trailheads)
    part2(m, trailheads)


if __name__ == "__main__":
    main()
