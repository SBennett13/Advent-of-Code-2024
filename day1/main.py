#!/usr/bin/env python3
### Day 1 AoC

from collections import Counter
import os.path

INPUT = os.path.join(os.path.abspath(os.path.dirname(__file__)), "input.txt")

def main() -> None:
    
    lhs = []
    rhs = []
    with open(INPUT, 'r') as f:
        for line in f.readlines():
            data = line.strip().split()
            lhs.append(int(data[0]))
            rhs.append(int(data[1]))

    lhs.sort()
    rhs.sort()
    count = Counter(rhs)
    distances = [abs(lh - rhs[i]) for i, lh in enumerate(lhs)]
    print(f"Total difference is {sum(distances)}")
    similarity = [val * count[val] for val in lhs]
    print(f"Similarity score is {sum(similarity)}")

if __name__ == "__main__":
    main()
