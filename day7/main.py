#!/usr/bin/env python3

import os

INPUT = os.path.join(os.path.abspath(os.path.dirname(__file__)), "input.txt")


def evaluate(result: int, vals: list[int], ops: tuple):
    # print(result, vals)
    if len(vals) == 1:
        return False
    for op in ops:
        # print(f"{vals[0]}{op}{vals[1]}")
        if op == "||":
            combine_ops = int(f"{vals[0]}{vals[1]}")
        else:
            combine_ops = eval(f"vals[0]{op}vals[1]")

        if result == combine_ops and len(vals) == 2:
            return True

        if evaluate(result, [combine_ops, *vals[2:]], ops):
            return True
    return False


def solve(data: dict[int, list[int]], ops: tuple):
    s = 0
    unsolved = {}

    for result, values in data.items():
        # print(result, values)
        preline_s = s
        for op in ops:
            if op == "||":
                comb = int(f"{values[0]}{values[1]}")
            else:
                comb = eval(f"values[0]{op}values[1]")
            if len(values) == 2 and result == comb:
                s += result
                break
            if evaluate(result, [comb, *values[2:]], ops):
                s += result
                break
        if preline_s == s:
            unsolved[result] = values
    return s, unsolved


def main():
    data = {}
    with open(INPUT) as f:
        for line in f.readlines():
            clean = line.strip()
            res, vals = clean.split(":")
            data[int(res)] = [int(v) for v in vals.strip().split(" ")]

    part1_sum, unsolved = solve(data, ("+", "*"))
    print(f"Part 1: {part1_sum}")
    part2_sum, _ = solve(unsolved, ("+", "*", "||"))
    print(f"Part 2: {part2_sum + part1_sum}")


if __name__ == "__main__":
    main()
