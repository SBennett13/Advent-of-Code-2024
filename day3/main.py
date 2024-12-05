#!/usr/bin/env python3
import os.path
import re

INPUT = os.path.join(os.path.abspath(os.path.dirname(__file__)), "input.txt")

part1_re = re.compile(r"mul\((?P<num1>[0-9]{1,3}),(?P<num2>[0-9]{1,3})\)")

do_dont_re = re.compile(r"(do|don't)\(\)")


def main() -> None:
    with open(INPUT) as f:
        data = f.read()
        nums = []
        change = []
        m = part1_re.search(data, 0)
        s1 = 0
        while m is not None:
            n1 = int(m.group("num1"))
            n2 = int(m.group("num2"))
            s1 += n1 * n2
            nums.append((m.start(), n1, n2))
            m = part1_re.search(data, m.end())
        m = do_dont_re.search(data, 0)
        while m is not None:
            change.append((m.start(), m.group()))
            m = do_dont_re.search(data, m.end())

        nums.extend(change)
        do = True
        s = 0
        for thing in sorted(nums, key=lambda x: x[0]):
            if len(thing) == 3 and do:
                s += thing[1] * thing[2]
            else:
                do = False if thing[1] == "don't()" else True
        print(f"Part 1: {s1}")
        print(f"Part 2: {s}")


if __name__ == "__main__":
    main()
