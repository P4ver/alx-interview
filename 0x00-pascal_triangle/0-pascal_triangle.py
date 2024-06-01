#!/usr/bin/python3
"""
- Pascal's Triangle.
"""


def pascal_triangle(n):
    """Create a function def pascal_triangle(n),
    """
    rs = []
    if n > 0:
        for i in range(1, n + 1):
            level = []
            C = 1
            for j in range(1, i + 1):
                level.append(C)
                C = C * (i - j) // j
            rs.append(level)
    return rs
