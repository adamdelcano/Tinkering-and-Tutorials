# https://leetcode.com/problems/matrix-cells-in-distance-order/submissions/

from typing import List


class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        """Given a matrix with R rows and C columns, with with integer
        coordinates (r, c) where 0 <= r < R and 0 <= c < C, and a specific
        cell in coordinates [r0, c0], returns a list of all cells in the
        matrix sorted by distance (smallest to largest, column first)."""
        matrix = []
        # Max distance between two cells is R + C - 2, thus this hits 0->Max
        for col_distance in range(0, (R + C - 1)):
            row_distance = 0
            # Loop through every row + column permutation that == distance
            while col_distance >= 0:
                # These have to check if it's inside the bounds of the matrix
                if c0 + col_distance < C:  # Column ceiling
                    if r0 + row_distance < R:  # Row ceiling
                        matrix.append([r0 + row_distance, c0 + col_distance])
                    if row_distance and r0 - row_distance >= 0:  # Row floor
                        matrix.append([r0 - row_distance, c0 + col_distance])
                if col_distance and c0 - col_distance >= 0:  # Column floor
                    if r0 + row_distance < R:  # Row ceiling
                        matrix.append([r0 + row_distance, c0 - col_distance])
                    if row_distance and r0 - row_distance >= 0:  # Row floor
                        matrix.append([r0 - row_distance, c0 - col_distance])
                col_distance -= 1
                row_distance += 1
        return matrix
