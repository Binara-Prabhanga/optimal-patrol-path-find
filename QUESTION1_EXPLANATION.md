# Question 1 Explanation

## 1(a) Transforming rectangles into points

Each rectangle is defined by two opposite corners: `(x1, y1)` and `(x2, y2)`.
Because the rectangles are axis-aligned, the only points that matter for the boundary of the patrol path are the rectangle corners.

For each rectangle, we extract its four corners:
- `(min(x1, x2), min(y1, y2))`
- `(min(x1, x2), max(y1, y2))`
- `(max(x1, x2), min(y1, y2))`
- `(max(x1, x2), max(y1, y2))`

Why corners?
- The patrol path must go around the outside of the rectangles.
- The rectangles are convex shapes, so the outer boundary of all rectangles is formed by their extreme corner points.
- Interior points or edge points are never needed for the shortest enclosing path if we consider all corners.

So the rectangle problem becomes a problem of finding a closed path around a set of points: all corner points of all rectangles.

## 1(b) Why the convex hull of corners is the optimal patrol path

The convex hull is the smallest convex polygon that contains a given set of points.

Why is this the best patrol path?
- A valid patrol path must enclose all rectangles and cannot pass through any rectangle interior.
- If the path is not convex, it has an inward bend or concave indentation.
- Any inward bend can be replaced by a straight line segment that is shorter and still keeps the path valid.
- Therefore, the shortest valid enclosing path must be convex.

The convex hull of all rectangle corners:
- includes every corner point on or inside the hull,
- is convex by definition,
- and is the tightest possible convex boundary around those points.

Because the rectangles are axis-aligned and their corners represent the outermost boundary points, the convex hull of these corners is exactly the optimal patrol path.

## 1(c) Algorithm to compute the convex hull

### Algorithm choice

We use **Andrew's monotone chain** algorithm.
This algorithm is easy to understand, easy to implement, and runs efficiently in `O(N log N)` time.

### Why sorting is needed

The first step is to sort the points by x-coordinate, and if x values are equal, by y-coordinate.
Sorting is needed because Andrew's algorithm builds the hull in two passes:
- one pass from left to right to build the lower hull,
- one pass from right to left to build the upper hull.

With sorted points, the algorithm can process points in a stable order and guarantee that the hull is built correctly without missing any extreme points.

### How cross products / orientation tests are used

For three points `O`, `A`, and `B`, we use the cross product:

```
cross(O, A, B) = (Ax - Ox) * (By - Oy) - (Ay - Oy) * (Bx - Ox)
```

This value tells us the turn direction from segment `OA` to segment `AB`:
- `> 0`: the turn is left (counter-clockwise)
- `< 0`: the turn is right (clockwise)
- `= 0`: the points are collinear

When building the hull, we keep only left turns.
If we encounter a right turn or a straight line, it means the previous point would make the boundary non-convex or longer than necessary, so we remove it from the hull.

### How the hull is built

1. Sort all points.
2. Build the lower hull:
   - Start from the leftmost point and move right.
   - Add each point to the hull.
   - While the last three points make a right turn or are collinear, remove the middle one.
3. Build the upper hull:
   - Start from the rightmost point and move left.
   - Repeat the same process.
4. Combine the lower and upper hulls, excluding the duplicate endpoints.

### Overall time complexity

Let `N` be the number of rectangles.
Each rectangle gives 4 corner points, so we handle `4N` points.

- Sorting the points: `O(N log N)`
- Building the lower hull: `O(N)`
- Building the upper hull: `O(N)`
- Computing the perimeter: `O(N)`

The overall time complexity is `O(N log N)`.

This is the best achievable complexity for convex hull algorithms that sort points first.
