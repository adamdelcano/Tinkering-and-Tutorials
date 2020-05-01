# https://leetcode.com/problems/matrix-cells-in-distance-order/submissions/

from typing import List


class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        """Given matrix with R rows and C columns, that has cells with integer
        coordinates (r, c), where 0 <= r < R and 0 <= c < C. Returns
        coordinates of all cells in the matrix, sorted by their distance from
        the initial cell, (r0, c0)."""
        matrix = {}
        for row in range(R):
            for column in range(C):
                distance = (abs(r0 - row) + abs(c0 - column))
                matrix.setdefault(distance, [])
                matrix[distance].append([row, column])
        matrix_list = []
        for key in range(R + C):
            matrix_list.extend(matrix.get(key, []))
        return matrix_list
