#!/usr/bin/env python3
from __future__ import annotations
import os
from dataclasses import dataclass

INPUT = os.path.join(os.path.abspath(os.path.dirname(__file__)), "input.txt")
EXAMPLE = os.path.join(os.path.abspath(os.path.dirname(__file__)), "example.txt")


@dataclass
class Location:
    r: int
    c: int

    def isAdjacent(self, rhs: Location):
        if abs(self.r - rhs.r) == 1 and self.c == rhs.c:
            return True
        elif abs(self.c - rhs.c) == 1 and self.r == rhs.r:
            return True
        else:
            return False

    def getSides(self):
        return [
            (self.r, self.r + 1, self.c, self.c),
            (self.r, self.r + 1, self.c + 1, self.c + 1),
            (self.r, self.r, self.c, self.c + 1),
            (self.r + 1, self.r + 1, self.c, self.c + 1),
        ]


@dataclass
class Region:
    locations: list[Location]

    def isOneRegion(self, rhs: Region):
        for n1 in self.locations:
            for n2 in rhs.locations:
                if n1.isAdjacent(n2):
                    return True

        return False

    def combine(self, rhs: Region):
        self.locations.extend(rhs.locations)

    def getArea(self):
        return len(self.locations)

    def getPerimeter(self):
        all_sides = []
        for i in self.locations:
            all_sides.extend(i.getSides())

        trimmed = []
        for ii, side in enumerate(all_sides):
            if side in all_sides[:ii] or side in all_sides[ii + 1 :]:
                continue
            trimmed.append(side)
        # print(trimmed)
        return len(trimmed), trimmed

    def getSides(self):
        perimeter = self.getPerimeter()[1]

        sides = [perimeter[0]]
        for post in perimeter[1:]:
            for i in range(len(sides)):
                dr = sides[i][0] + sides[i][1] + post[0] + post[1]
                dc = sides[i][2] + sides[i][3] + post[2] + post[3]
                if (dr == 0 and dc != 0) or (dr != 0 and dc == 0):
                    print(f"Post {post} extends side {sides[i]}")
                    sides[i] = (
                        min(sides[i][0], sides[i][1], post[0], post[1]),
                        max(sides[i][0], sides[i][1], post[0], post[1]),
                        min(sides[i][2], sides[i][3], post[2], post[3]),
                        max(sides[i][2], sides[i][3], post[2], post[3]),
                    )
                    print(f"New side: {sides[i]}")
                    break
            else:
                sides.append(post)
        return 0


def regionify(locations: list[Location], regions: list[Region]):
    regions.append(Region([locations[0]]))
    for location in locations[1:]:
        correct_region = -1
        for ri, region in enumerate(regions):
            for point in region.locations:
                if location.isAdjacent(point):
                    # print(f"{location} is near {point} in region {ri}")
                    correct_region = ri
                    break
            if correct_region != -1:
                break
        if correct_region == -1:
            # print(f"Putting {location} in its own region")
            regions.append(Region([location]))
        else:
            # print(f"Adding {location} to region {regions[correct_region]}")
            regions[correct_region].locations.append(location)

    if len(regions) > 1:
        done = False
        while not done:
            for i, reg in enumerate(regions):
                did_comb = False
                for ii in range(i + 1, len(regions)):
                    if reg.isOneRegion(regions[ii]):
                        # print(f"Should combine {reg} & {regions[ii]}")
                        reg.combine(regions[ii])
                        regions.pop(ii)
                        did_comb = True
                        break
                if did_comb:
                    break
            if not did_comb:
                done = True


def part1(locations: dict[str, list[Location]]):
    regions: dict[str, list[Region]] = {}
    # Separate into regions
    for t in locations:
        print(f"Making regions of {t}")
        regions[t] = []
        regionify(locations[t], regions[t])

    total = 0
    for t in regions:
        # print(f"Regions of {t}:")
        for rg in regions[t]:
            # print(f"{rg}")
            total += rg.getArea() * rg.getPerimeter()[0]
        # print("---------")

    print(f"Part 1: {total}")
    return regions


def part2(regions: dict[str, list[Region]], /):
    total = 0
    for t in regions:
        for rg in regions[t]:
            total += rg.getArea() * rg.getSides()
    print(f"Part 2: {69}")


def main():
    m = []
    locs = {}
    with open(EXAMPLE) as f:
        r = 0
        for line in f.readlines():
            m.append(line.strip())
            for c, char in enumerate(m[-1]):
                if char not in locs:
                    locs[char] = []
                locs[char].append(Location(r, c))
            r += 1

    regions = part1(locs)
    part2(regions)


if __name__ == "__main__":
    main()
