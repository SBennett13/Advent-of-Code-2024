#!/usr/bin/env python3

import os
from collections import namedtuple
from copy import deepcopy

INPUT = os.path.join(os.path.abspath(os.path.dirname(__file__)), "input.txt")

Position = namedtuple("Position", ["r", "c"])
Step = namedtuple(
    "Step",
    [
        "position",
    ],
)


def get_next_position(
    m: list[str], current_position: Position, direction: int
) -> tuple[Position, int] | int | None:
    start_direction = direction
    for _ in range(4):
        if direction == 0:
            update = (-1, 0)
        elif direction == 1:
            update = (0, 1)
        elif direction == 2:
            update = (1, 0)
        elif direction == 3:
            update = (0, -1)

        next_position = Position(
            r=current_position.r + update[0], c=current_position.c + update[1]
        )
        if (
            next_position.r >= len(m)
            or next_position.r < 0
            or next_position.c >= len(m[0])
            or next_position.c < 0
        ):
            return None

        if m[next_position.r][next_position.c] == "#":
            direction = (direction + 1) % 4
            if direction == start_direction:
                return -1
        else:
            return (next_position, direction)


def part1(m: list[str], guard_start: Position):
    visited: set[Position] = set()
    path: list[tuple[Position, int]] = []
    guard_direction = 0

    guard_position = guard_start
    done = False

    while not done:
        visited.add(guard_position)
        path.append((guard_position, guard_direction))
        n = get_next_position(m, guard_position, guard_direction)
        if n is None:
            print(f"Part 1: {len(visited)}")
            return path
        guard_position = n[0]
        guard_direction = n[1]


def check_location(
    m2: list[str],
    location: tuple[Position, int],
    path: list[tuple[Position, int]],
    /,
) -> bool:
    line: str = m2[location[0].r]
    line2 = line[: location[0].c] + "#"
    if location[0].c != len(m2[0]) - 1:
        line2 += line[location[0].c + 1 :]
    m2[location[0].r] = line2
    guard_direction = path[-1][1]
    guard_position = path[-1][0]

    while True:
        n = get_next_position(m2, guard_position, guard_direction)
        if n is None:
            return False
        elif n == -1:
            print("WHAT")
            return False

        path.append(n)
        guard_direction = n[1]
        guard_position = n[0]
        if n in path[:-1]:
            return True


def part2(m: list[str], p: list[tuple[Position, int]]):
    num_locs = 0
    checked = []
    for i, loc in enumerate(p[1:]):
        if loc[0] in checked:
            # print(f"Already checked {loc[0]}")
            continue

        checked.append(loc[0])
        mcpy = deepcopy(m)
        # print(f"Checking {loc[0]}")
        if check_location(mcpy, loc, p[: i + 1]):
            num_locs += 1

    print(f"Part 2: {num_locs}")


def main():
    the_map = []
    guard_start: Position = None
    with open(INPUT) as f:
        for r_i, line in enumerate(f.readlines()):
            the_map.append(line.strip())
            try:
                idx = line.index("^")
            except ValueError:
                pass
            else:
                guard_start = Position(r=r_i, c=idx)

    path = part1(the_map, guard_start)
    part2(the_map, path)


if __name__ == "__main__":
    main()
