#!/usr/bin/env python3

import os
import re

INPUT = os.path.join(os.path.abspath(os.path.dirname(__file__)), "input.txt")
EXAMPLE = os.path.join(os.path.abspath(os.path.dirname(__file__)), "example.txt")

button_re = re.compile(r"Button (?P<button>A|B): X\+(?P<xval>\d+), Y\+(?P<yval>\d+)")
prize_re = re.compile(r"Prize: X=(?P<xval>\d+), Y=(?P<yval>\d+)")

A_COST = 3
B_COST = 1


def part1(inputs: list, part=1):
    s = 0
    for i in inputs:
        a1 = i["A"]["x"]
        b1 = i["B"]["x"]
        a2 = i["A"]["y"]
        b2 = i["B"]["y"]
        c1 = -1 * i["prize"]["x"]
        c2 = -1 * i["prize"]["y"]
        x = (b1 * c2 - b2 * c1) / (b2 * a1 - b1 * a2)
        y = (c1 * a2 - c2 * a1) / (b2 * a1 - b1 * a2)
        if x.is_integer() and y.is_integer():
            s += int(x) * A_COST + int(y) * B_COST

    print(f"Part {part}: {s}")


def part2(inputs: list):
    for i in inputs:
        i["prize"]["x"] += 10000000000000
        i["prize"]["y"] += 10000000000000

    part1(inputs, 2)


def main():
    inputs = []

    with open(INPUT) as f:
        for line in f:
            result = {}
            m = button_re.match(line.strip())
            result[m.group("button")] = {
                "x": int(m.group("xval")),
                "y": int(m.group("yval")),
            }
            line = f.readline()
            m = button_re.match(line.strip())
            result[m.group("button")] = {
                "x": int(m.group("xval")),
                "y": int(m.group("yval")),
            }
            line = f.readline()
            m = prize_re.match(line.strip())
            result["prize"] = {"x": int(m.group("xval")), "y": int(m.group("yval"))}
            f.readline()
            inputs.append(result)

    part1(inputs)
    part2(inputs)


if __name__ == "__main__":
    main()
