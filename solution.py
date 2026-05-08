#!/usr/bin/env python3
"""
Optimal Patrol Path Around Machines
Finds the shortest closed path that encloses all rectangular machines
using convex hull of rectangle corners.
"""

import math
from typing import List, Tuple

Point = Tuple[float, float]


def cross_product(o: Point, a: Point, b: Point) -> float:
    """
    Compute cross product of vectors OA and OB.
    Returns (A.x - O.x) * (B.y - O.y) - (A.y - O.y) * (B.x - O.x)
    Positive = left turn, Negative = right turn, Zero = collinear
    """
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def distance(p1: Point, p2: Point) -> float:
    """Compute Euclidean distance between two points."""
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)


def convex_hull(points: List[Point]) -> List[Point]:
    """
    Compute convex hull using Andrew's monotone chain algorithm.
    Returns list of points on convex hull in counter-clockwise order.
    Time complexity: O(n log n) due to sorting.
    """
    if len(points) <= 2:
        return points

    points = sorted(set(points))

    if len(points) <= 2:
        return points

    lower = []
    for p in points:
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]


def perimeter(hull: List[Point]) -> float:
    """Compute perimeter as sum of distances along the convex hull."""
    if len(hull) < 2:
        return 0.0

    total = 0.0
    for i in range(len(hull)):
        total += distance(hull[i], hull[(i + 1) % len(hull)])

    return total


def extract_corners(x1: float, y1: float, x2: float, y2: float) -> List[Point]:
    """Extract four corners of an axis-aligned rectangle."""
    min_x, max_x = min(x1, x2), max(x1, x2)
    min_y, max_y = min(y1, y2), max(y1, y2)
    return [
        (min_x, min_y),
        (min_x, max_y),
        (max_x, min_y),
        (max_x, max_y),
    ]


def solve() -> float:
    """Main solution: read input, compute convex hull, return perimeter."""
    n = int(input())
    all_corners = []

    for _ in range(n):
        x1, y1, x2, y2 = map(float, input().split())
        corners = extract_corners(x1, y1, x2, y2)
        all_corners.extend(corners)

    hull = convex_hull(all_corners)
    return perimeter(hull)


if __name__ == "__main__":
    result = solve()
    print(f"{result:.10f}")
