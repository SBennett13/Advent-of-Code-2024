#!/usr/bin/env python3
import os.path
from copy import deepcopy

INPUT = os.path.join(os.path.abspath(os.path.dirname(__file__)), "input.txt")


def check_diff_sorted(inval, increasing: bool):
    for idx, val in enumerate(inval):
        if idx == 0:
            continue
        diff = val - inval[idx - 1] if increasing else inval[idx - 1] - val
        if diff > 3 or diff < 1:
            return False

    return True


def check_bads(inval) -> bool:
    for i in range(len(inval)):
        cpy: list = deepcopy(inval)
        cpy.pop(i)
        valid = check_diff_sorted(cpy, cpy[0] < cpy[1])
        if valid:
            return True
    return False


def main():
    valid = 0
    perms = 0
    with open(INPUT) as f:
        for line in f.readlines():
            clean_line = [int(i) for i in line.strip().split()]
            if check_diff_sorted(clean_line, clean_line[1] > clean_line[0]):
                valid += 1
            elif check_bads(clean_line):
                perms += 1

    print(f"Num Valid: {valid}")
    print(f"Num Valid with perms: {valid + perms}")


if __name__ == "__main__":
    main()
