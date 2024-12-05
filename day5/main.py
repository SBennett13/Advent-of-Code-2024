#!/usr/bin/env python3

import math
import os

INPUT = os.path.join(os.path.abspath(os.path.dirname(__file__)), "input.txt")


def part1(rules: dict[int,list[int]], updates: list[list[int]]):
    ans = 0
    incorrect = []
    for update in updates:
        for i,curr in enumerate(update):
            valid = True
            for ii in range(0,i):
                if update[ii] in rules[curr]:
                    valid = False
                    break
            if valid is False:
                incorrect.append(update)
                break
        else:
            val = update[math.floor(len(update)/2)]
            ans += val
        
    print(f"part 1: {ans}")
    return incorrect


# Part2
def sort_insert(order: list[int], item: int, rule: list[int]):
    earliest = len(order)
    for r in rule:
        try:
            r_i = order.index(r)
        except ValueError:
            continue
        if r_i < earliest:
            earliest = r_i
    order.insert(earliest, item)

def part2(updates: list[int], rules:dict[int, list[int]]):
    ans = 0
    for update in updates:
        
        new_order = [update[0]]
        for u in update[1:]:
            sort_insert(new_order, u, rules[u])
        ans += new_order[math.floor(len(new_order)/2)]

    print(f"part 2: {ans}")
    return


def main() -> None:
    order_rules = {}
    updates = []
    state = 0
    with open(INPUT) as f:
        for line in f.readlines():
            line = line.strip()
            if not line:
                state += 1
                continue
            if state == 0:
                a,b = line.split("|")
                if int(a) not in order_rules:
                    order_rules[int(a)] = []
                order_rules[int(a)].append(int(b))
            else:
                updates.append([int(i) for i in line.split(",")])

    incorrect_updates = part1(order_rules, updates)
    part2(incorrect_updates, order_rules)

if __name__ == "__main__":
    main()
