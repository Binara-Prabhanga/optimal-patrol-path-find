# Optimal Patrol Path

This repository solves the problem of finding the shortest closed patrol path that encloses all axis-aligned rectangular machines without passing through their interiors.

## Solution Summary

- Convert each rectangle into its 4 corner points.
- Compute the convex hull of all corner points using Andrew's monotone chain algorithm.
- The convex hull is the shortest valid patrol path that encloses all rectangles.
- Output the perimeter of the convex hull with 10 decimal places.

## Why the Convex Hull is the Optimal Path

1. A valid enclosing path must surround every rectangle and cannot enter rectangle interiors.
2. Any shortest enclosing path must be convex, because a concave path can be shortened by eliminating inward bends.
3. The convex hull of all rectangle corners is the tightest convex boundary enclosing the rectangles.
4. Therefore, the convex hull gives the shortest valid patrol path.

## Algorithm Used

### 1. Transform rectangles to points

For each rectangle defined by opposite corners `(x1, y1)` and `(x2, y2)`, extract:
- `(min(x1, x2), min(y1, y2))`
- `(min(x1, x2), max(y1, y2))`
- `(max(x1, x2), min(y1, y2))`
- `(max(x1, x2), max(y1, y2))`

This produces the four corner points for the rectangle.

### 2. Compute the convex hull

Use Andrew's monotone chain algorithm:
- Sort points lexicographically by `(x, y)`.
- Build the lower hull from left to right.
- Build the upper hull from right to left.
- Remove duplicate endpoints and concatenate.

### 3. Compute the perimeter

Sum Euclidean distances between successive hull points and close the polygon.

## Mathematical Formulas

### Cross product / orientation test

For points `O = (ox, oy)`, `A = (ax, ay)`, `B = (bx, by)`:

```
cross(O, A, B) = (ax - ox)*(by - oy) - (ay - oy)*(bx - ox)
```

- `> 0`: left turn (counter-clockwise)
- `< 0`: right turn (clockwise)
- `= 0`: collinear

### Euclidean distance

```
distance(P1, P2) = sqrt((x2 - x1)^2 + (y2 - y1)^2)
```

### Perimeter of convex hull

```
perimeter = sum(distance(v_i, v_{i+1})) for all consecutive hull points, closing the loop
```

## Complexity

- Input parsing: `O(N)`
- Corner extraction: `O(N)`
- Sorting points: `O(N log N)`
- Hull construction: `O(N)`
- Perimeter calculation: `O(K)` where `K` is hull size

**Total time complexity:** `O(N log N)`

## Files Included

- `solution.py` — implementation of the patrol-path solver
- `README.md` — project description and answer summary
- `test.py` — basic validation tests for the solution helpers

## Usage

Run with Python 3:

```bash
python solution.py < input.txt
```

The program reads the number of rectangles and their coordinates, then prints the shortest patrol path perimeter.
