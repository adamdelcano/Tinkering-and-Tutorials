# https://leetcode.com/problems/matrix-cells-in-distance-order/submissions/

from typing import List


class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        matrix = []
        for row in range(R):  # create the whole matrix from scratch
            for column in range(C):
                matrix.append([row, column])
        matrix.sort(key=lambda cell: abs(r0 - cell[0]) + abs(c0 - cell[1]))
        return matrix
