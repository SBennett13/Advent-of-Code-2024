#!/usr/bin/env python3

from collections import namedtuple
import os

INPUT = os.path.join(os.path.abspath(os.path.dirname(__file__)), "input.txt")


Location = namedtuple("Location", ["r", "c"])


def process1(m: list[str], locs: list[Location]):
    antinode_locs = set()
    for i, a1 in enumerate(locs):
        for j in range(i + 1, len(locs)):
            a2 = locs[j]

            # Solve the midpoint formula each direction
            r1 = 2 * a1.r - a2.r
            c1 = 2 * a1.c - a2.c
            r2 = 2 * a2.r - a1.r
            c2 = 2 * a2.c - a1.c

            for r, c in ((r1, c1), (r2, c2)):
                if r >= len(m) or r < 0 or c >= len(m[0]) or c < 0:
                    continue
                antinode_locs.add(Location(r, c))
    return antinode_locs


def part1(m: list[str], antennas: dict[str, list[Location]]):
    antinodes = set()
    for locs in antennas.values():
        antinodes.update(process1(m, locs))

    print(f"Part 1: {len(antinodes)}")


def process2(m: list[str], locs: list[Location]):
    antinode_locs = set()
    for i, a1 in enumerate(locs):
        for j in range(i + 1, len(locs)):
            a2 = locs[j]

            # Calc distance between them
            dr = a1.r - a2.r
            dc = a1.c - a2.c

            # Iterate out each direction
            for iii in range(2):
                mult = 1 if iii == 0 else -1
                last = a2 if iii == 0 else a1
                # Go until we run off the board
                while True:
                    nr, nc = last.r + dr * mult, last.c + dc * mult
                    if nr >= len(m) or nr < 0 or nc >= len(m[0]) or nc < 0:
                        break
                    loc = Location(nr, nc)
                    antinode_locs.add(loc)
                    last = loc

    return antinode_locs


def part2(m: list[str], antennas: dict[str, list[Location]]):
    antinodes = set()
    for locs in antennas.values():
        antinodes.update(process2(m, locs))

    print(f"Part 2: {len(antinodes)}")


def main():
    m = []
    antennas: dict[str, list[Location]] = {}
    with open(INPUT) as f:
        r = 0
        for line in f.readlines():
            line = line.strip()
            for c, char in enumerate(line):
                if char == ".":
                    continue
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append(Location(r, c))
            m.append(line)
            r += 1

    part1(m, antennas)
    part2(m, antennas)


if __name__ == "__main__":
    main()
