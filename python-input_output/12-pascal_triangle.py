#!/usr/bin/python3
"""Pascal triangle module."""


def pascal_triangle(n):
    """Return Pascal's triangle as a list of lists."""
    tlist = []
    if n <= 0:
        return tlist

    tlist = [[1]]

    for i in range(n - 1):
        temp = [0] + tlist[-1] + [0]
        row = []

        for j in range(len(temp) - 1):
            row.append(temp[j] + temp[j + 1])

        tlist.append(row)
    return tlist
