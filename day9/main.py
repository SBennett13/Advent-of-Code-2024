#!/usr/bin/env python3

from copy import deepcopy
import os


INPUT = os.path.join(os.path.abspath(os.path.dirname(__file__)), "input.txt")


def part1(data: str, counts):
    result = []
    is_block = True
    # iterate over the block and copy in the values
    for i in range(len(data)):
        if not counts:
            break

        # If data block, just copy to result
        if is_block:
            key_out = min(counts.keys())
            num = counts.pop(key_out)
            result.extend([key_out for _ in range(num)])
        else:
            # Get the number of entries needed and remove max val'd keys until satisfied
            entries_needed = int(data[i])
            extension = []
            while entries_needed != 0:
                max_key = max(counts.keys())
                if counts[max_key] < entries_needed:
                    num = counts.pop(max_key)
                    entries_needed -= num
                    extension.extend([max_key for _ in range(num)])
                else:
                    counts[max_key] -= entries_needed
                    if counts[max_key] == 0:
                        counts.pop(max_key)
                    extension.extend([max_key for _ in range(entries_needed)])
                    entries_needed = 0
            result.extend(extension)

        is_block = not is_block

    s = 0
    for idx, val in enumerate(result):
        s += idx * val
    print(f"Part 1: {s}")


def part2(counts: dict[int, int], spaces: list[int]):
    from collections import namedtuple

    Block = namedtuple("Block", ["start_idx", "span", "id"])
    space_blocks: list[Block] = []
    data_blocks: dict[int, Block] = {}
    drive_idx = 0
    for idx, val in enumerate(spaces):
        data_blocks[idx] = Block(drive_idx, counts[idx], idx)
        drive_idx += counts[idx]
        space_blocks.append(Block(drive_idx, val, -1))
        drive_idx += val

    max_count = max(counts.keys())
    data_blocks[max_count] = Block(drive_idx, counts[max_count], max_count)

    for i in sorted(counts.keys(), reverse=True):
        spaces_needed = counts[i]
        for b_i in range(len(space_blocks)):
            if space_blocks[b_i].start_idx >= data_blocks[i].start_idx:
                break
            if space_blocks[b_i].span >= spaces_needed:
                b = space_blocks[b_i]
                # print(f"Placing block {data_blocks[i]} starting at idx {b.start_idx}")
                data_blocks[i] = Block(
                    b.start_idx, data_blocks[i].span, data_blocks[i].id
                )
                new_span = b.span - data_blocks[i].span
                if not new_span:
                    space_blocks.pop(b_i)
                else:
                    new_start = b.start_idx + data_blocks[i].span
                    space_blocks[b_i] = Block(new_start, new_span, -1)

                break
        else:
            print(f"Couldn't move {data_blocks[i]}")

    s = 0
    sorted_drive = sorted(data_blocks.values(), key=lambda b: b.start_idx)
    for b in sorted_drive:
        start_idx = b.start_idx
        for i in range(b.span):
            s += b.id * (start_idx + i)

    print(f"Part 2: {s}")


def main():
    data = ""
    with open(INPUT) as f:
        data = f.read()

    # Get the count of everything
    id_cnt = 0
    counts = {}
    spaces = []
    for i in range(len(data)):
        if i % 2 == 0:
            counts[id_cnt] = int(data[i])
            id_cnt += 1
        else:
            spaces.append(int(data[i]))

    part1(deepcopy(data), deepcopy(counts))
    part2(counts, spaces)


if __name__ == "__main__":
    main()
