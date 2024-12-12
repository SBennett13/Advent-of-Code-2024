#!/usr/bin/env python3

import os

INPUT = os.path.join(os.path.abspath(os.path.dirname(__file__)), "input.txt")

EXAMPLE = os.path.join(os.path.abspath(os.path.dirname(__file__)), "example.txt")


def blink(in_data: str):
    if in_data == "0":
        return ["1"]
    el_len = len(in_data)
    if el_len % 2 == 0:
        return [
            str(int(in_data[: (el_len // 2)])),
            str(int(in_data[el_len // 2 :])),
        ]
    else:
        return [str(int(in_data) * 2024)]


def part1_2(
    data: list[str],
):
    s = 0
    from collections import defaultdict

    stone1 = defaultdict(lambda: 0)
    stone2 = defaultdict(lambda: 0)
    for i in data:
        stone1[i] += 1
    for _ in range(75):
        for stone, occ in stone1.items():
            out = blink(stone)
            for stone_o in out:
                stone2[stone_o] += 1 * occ
        stone1 = stone2
        stone2 = defaultdict(lambda: 0)
        if _ == 24:
            s_1 = 0
            for i in stone1.values():
                s_1 += i
            print(f"Part 1: {s_1}")

    for i in stone1.values():
        s += i

    print(f"Part 2: {s}")


def main():
    data = []
    with open(INPUT) as f:
        for line in f.readlines():
            data.extend(line.strip().split(" "))

    part1_2(data)


if __name__ == "__main__":
    main()
