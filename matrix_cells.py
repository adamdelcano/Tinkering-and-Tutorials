# https://leetcode.com/problems/matrix-cells-in-distance-order/submissions/

from typing import List


class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        """Given matrix with R rows and C columns, that has cells with integer
        coordinates (r, c), where 0 <= r < R and 0 <= c < C. Returns
        coordinates of all cells in the matrix, sorted by their distance from
        the initial cell, (r0, c0)."""
        matrix = []
        for col_distance in range(0, (R + C - 1)):
            row_distance = 0
            while col_distance >= 0:
                if c0 + col_distance < C:  # Column upper bound check
                    if r0 + row_distance < R:  # Row upper bound check
                        matrix.append([r0 + row_distance, c0 + col_distance])
                    if row_distance and r0 - row_distance >= 0:  # and lower
                        matrix.append([r0 - row_distance, c0 + col_distance])
                if col_distance and c0 - col_distance >= 0:  # col lower bound
                    if r0 + row_distance < R:  # Row upper bound check
                        matrix.append([r0 + row_distance, c0 - col_distance])
                    if row_distance and r0 - row_distance >= 0:  # and lower
                        matrix.append([r0 - row_distance, c0 - col_distance])
                col_distance -= 1
                row_distance += 1
        return matrix
