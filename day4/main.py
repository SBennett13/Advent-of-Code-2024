#!/usr/bin/env python3
from copy import deepcopy
from collections import Counter
import os

INPUT = os.path.join(os.path.abspath(os.path.dirname(__file__)), "input.txt")


def look(
    grid: list, idx: int, direction: int, where: list, nrow: int, ncol: int, key: str
):
    cur_r = where[-1][0]
    cur_i = where[-1][1]

    # print(f"cur_r,cur_i: ({cur_r},{cur_i}) | direction: {direction}")
    if direction == 0:
        # N
        cur_r -= 1
    elif direction == 1:
        # NE
        cur_r -= 1
        cur_i += 1
    elif direction == 2:
        # E
        cur_i += 1
    elif direction == 3:
        # SE
        cur_i += 1
        cur_r += 1
    elif direction == 4:
        # S
        cur_r += 1
    elif direction == 5:
        # SW
        cur_r += 1
        cur_i -= 1
    elif direction == 6:
        # W
        cur_i -= 1
    elif direction == 7:
        # NW
        cur_r -= 1
        cur_i -= 1

    if cur_r < 0 or cur_r >= nrow:
        return False
    if cur_i < 0 or cur_i >= ncol:
        return False
    if grid[cur_r][cur_i] == key[idx]:
        if key[idx] == key[-1]:
            return True
        new_where = deepcopy(where)
        new_where.append((cur_r, cur_i))
        return look(grid, idx + 1, direction, new_where, nrow, ncol, key)
    return False


def look2(
    grid: list, direction: int, where: list[tuple], nrow: int, ncol: int, valid: tuple
):
    cur_r = where[0][0]
    cur_i = where[0][1]

    # print(f"cur_r,cur_i: ({cur_r},{cur_i}) | direction: {direction}")
    if direction == 0:
        # N
        cur_r -= 1
    elif direction == 1:
        # NE
        cur_r -= 1
        cur_i += 1
    elif direction == 2:
        # E
        cur_i += 1
    elif direction == 3:
        # SE
        cur_i += 1
        cur_r += 1
    elif direction == 4:
        # S
        cur_r += 1
    elif direction == 5:
        # SW
        cur_r += 1
        cur_i -= 1
    elif direction == 6:
        # W
        cur_i -= 1
    elif direction == 7:
        # NW
        cur_r -= 1
        cur_i -= 1

    if cur_r < 0 or cur_r >= nrow:
        return "N"
    if cur_i < 0 or cur_i >= ncol:
        return "N"

    where.append((cur_r, cur_i))
    return grid[cur_r][cur_i]


def xmas(grid: list, key="XMAS"):
    count = 0
    for r_i, r in enumerate(grid):
        for c_i, c in enumerate(r):
            if c != key[0]:
                continue
            for direction in range(0, 8):
                found = look(
                    grid, 1, direction, [(r_i, c_i)], len(grid), len(grid[0]), key
                )
                if found:
                    count += 1

    print(f"part 1 : {count}")


# Part 2
def x_mas(grid: list, key="MAS"):
    count = 0
    for r_i, r in enumerate(grid):
        for c_i, c in enumerate(r):
            if c != key[1]:
                continue
            counter = Counter(A=1)
            locations = [(r_i, c_i)]
            for direction in range(1, 8, 2):
                counter[
                    look2(grid, direction, locations, len(grid), len(grid), ("M", "S"))
                ] += 1
            if counter["N"] or counter["X"]:
                continue
            #print(counter)
            if (
                counter["A"] == 1
                and counter["M"] == 2
                and counter["S"] == 2
                and check_x(grid, locations)
            ):
                #print(f"found with locations: ({locations})")
                count += 1
    print(f"part 2 : {count}")


def check_x(grid: list, locations: list) -> bool:
    center = locations[0]
    for x in range(-1, 2, 2):
        for y in range(-1, 2, 2):
            if (center[0] + x, center[1] + y) not in locations:
                return False
    if (
        grid[center[0] + 1][center[1] + 1] == grid[center[0] - 1][center[1] - 1]
        or grid[center[0] + 1][center[1] - 1] == grid[center[0] - 1][center[1] + 1]
    ):
        return False
    return True


def main() -> None:
    grid = []
    with open(INPUT) as f:
        for line in f.readlines():
            grid.append(line.strip())

    xmas(grid)
    x_mas(grid)


if __name__ == "__main__":
    main()
