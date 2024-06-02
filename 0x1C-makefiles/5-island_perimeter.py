#!/usr/bin/python3

"""
5-island_perimeter.py

This module defines a function `island_perimeter` that calculates the perimeter
of the island in a rectangular grid.

The grid is represented as a list of lists of integers:
    - 0 represents a water zone
    - 1 represents a land zone

The function assumes the following:
    - Grid cells are connected horizontally/vertically (not diagonally).
    - Grid is rectangular, width and height don't exceed 100
    - Grid is completely surrounded by water, and there is one island (or nothing).
    - The island doesn't have "lakes" (water inside that isn't connected to the water around the island).

Args:
    grid: A list of lists of integers representing the grid.

Returns:
    The perimeter of the island in the grid, or 0 if there is no island.
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island in the provided grid.

    The perimeter is calculated by counting the number of edges of land cells
    that are adjacent to water cells.

    Args:
        grid: A list of lists of integers representing the grid.

    Returns:
        The perimeter of the island in the grid, or 0 if there is no island.
    """

    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                # Check for water neighbors (up, down, left, right)
                perimeter += 4  # Assume all sides are water initially

                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2  # Not water on top

                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2  # Not water on left

    return perimeter

# This part is for running the function as a script if executed directly
if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
