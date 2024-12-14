#!/usr/bin/env python3

from collections import defaultdict
import os
import re

INPUT = os.path.join(os.path.abspath(os.path.dirname(__file__)), "input.txt")
EXAMPLE = os.path.join(os.path.abspath(os.path.dirname(__file__)), "example.txt")

line_re = re.compile(r"p=(?P<px>\d+),(?P<py>\d+) v=(?P<vx>-{0,1}\d+),(?P<vy>-{0,1}\d+)")

X, Y = 101, 103
# X, Y = 11, 7

MID_X, MID_Y = X // 2, Y // 2


def printBoard(guards):
    board = []
    for _ in range(Y):
        board.append(["." for _ in range(X)])

    for guard in guards:
        board[guard["y"]][guard["x"]] = "#"

    for row in board:
        print("".join(row))


def getScore(guards: list[dict]):
    sections = defaultdict(lambda: 0)
    for guard in guards:
        if guard["x"] == MID_X or guard["y"] == MID_Y:
            continue

        if guard["x"] < MID_X:
            if guard["y"] < MID_Y:
                sections[0] += 1
            else:
                sections[1] += 1
        else:
            if guard["y"] < MID_Y:
                sections[2] += 1
            else:
                sections[3] += 1

    s = 0
    for i in sections.values():
        if s == 0:
            s = i
        else:
            s *= i
    return s


def iterate(guards: list[dict]):
    for guard in guards:
        guard["x"] += guard["vx"]
        guard["y"] += guard["vy"]
        if guard["x"] < 0:
            guard["x"] = X + guard["x"]
        elif guard["x"] >= X:
            guard["x"] -= X
        if guard["y"] < 0:
            guard["y"] += Y
        elif guard["y"] >= Y:
            guard["y"] -= Y


def part1(guards: list[tuple], iterations: int):
    for _ in range(iterations):
        iterate(guards)
    s = getScore(guards)
    print(f"Part 1: {s}")


def part2(guards: list[dict]):
    try:
        minimum = 1e12
        i = 0
        min_i = 0
        while True:
            i += 1
            iterate(guards)
            s = getScore(guards)
            if s < minimum:
                minimum = s
                min_i = i
                printBoard(guards)
                print(f"Seconds elapsed: {i}")
                input()
    except KeyboardInterrupt:
        pass

    print(f"Part 2: {min_i}")

    return


def main():
    guards = []
    with open(INPUT) as f:
        for line in f.readlines():
            m = line_re.match(line.strip())
            guards.append(
                {
                    "x": int(m.group("px")),
                    "y": int(m.group("py")),
                    "vx": int(m.group("vx")),
                    "vy": int(m.group("vy")),
                }
            )

    from copy import deepcopy

    part1(deepcopy(guards), 100)
    part2(guards)


if __name__ == "__main__":
    main()
