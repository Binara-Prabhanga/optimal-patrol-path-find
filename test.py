#!/usr/bin/env python3
"""Test cases for the optimal patrol path solution."""

from solution import (
    cross_product,
    distance,
    convex_hull,
    perimeter,
    extract_corners,
)


def test_cross_product():
    """Test cross product orientation."""
    o = (0, 0)
    a = (1, 0)
    b = (0, 1)
    assert cross_product(o, a, b) > 0  # left turn
    assert cross_product(o, b, a) < 0  # right turn
    assert cross_product(o, a, (2, 0)) == 0  # collinear
    print("✓ cross_product tests pass")


def test_distance():
    """Test Euclidean distance."""
    assert abs(distance((0, 0), (3, 4)) - 5.0) < 1e-9
    assert abs(distance((0, 0), (0, 0)) - 0.0) < 1e-9
    print("✓ distance tests pass")


def test_extract_corners():
    """Test rectangle corner extraction."""
    corners = extract_corners(0, 0, 2, 3)
    assert len(corners) == 4
    assert (0, 0) in corners
    assert (2, 3) in corners
    print("✓ extract_corners tests pass")


def test_convex_hull_square():
    """Test convex hull of a simple square."""
    points = [(0, 0), (1, 0), (1, 1), (0, 1)]
    hull = convex_hull(points)
    assert len(hull) == 4
    print("✓ convex_hull (square) tests pass")


def test_perimeter_square():
    """Test perimeter of unit square."""
    square = [(0, 0), (1, 0), (1, 1), (0, 1)]
    perim = perimeter(square)
    assert abs(perim - 4.0) < 1e-9
    print("✓ perimeter (square) tests pass")


def test_single_rectangle():
    """Test single rectangle input."""
    # Rectangle from (0,0) to (2,2) should have perimeter 8
    corners = extract_corners(0, 0, 2, 2)
    hull = convex_hull(corners)
    perim = perimeter(hull)
    assert abs(perim - 8.0) < 1e-9
    print("✓ single_rectangle tests pass")


def test_two_adjacent_rectangles():
    """Test two adjacent unit squares side by side."""
    # Square 1: (0,0) to (1,1)
    # Square 2: (1,0) to (2,1)
    # Should form a 2x1 rectangle with perimeter 6
    corners = extract_corners(0, 0, 1, 1) + extract_corners(1, 0, 2, 1)
    hull = convex_hull(corners)
    perim = perimeter(hull)
    assert abs(perim - 6.0) < 1e-9
    print("✓ two_adjacent_rectangles tests pass")


if __name__ == "__main__":
    test_cross_product()
    test_distance()
    test_extract_corners()
    test_convex_hull_square()
    test_perimeter_square()
    test_single_rectangle()
    test_two_adjacent_rectangles()
    print("\n All tests passed!")
