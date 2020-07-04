# for https://leetcode.com/problems/reshape-the-matrix/
from typing import List


class Solution:
    """ Implements matlab's reshape function: given a matrix nums, reshapes it
    into a different size of r rows and c columns while maintaining the
    elements in row-traversing order. If imposible returns original. """
    def matrixReshape(
        self, nums: List[List[int]], r: int, c: int
    ) -> List[List[int]]:
        original_r = len(nums)
        original_c = len(nums[0])
        # check if it can be reshaped
        if (original_r * original_c) != (r * c):
            return nums
        # create a new empty matrix to populate
        new_list = [[0] * c for row in range(r)]
        for row_index, row in enumerate(nums):
            for column_index, num in enumerate(row):
                # I EXTREMELY did not think of this math myself
                flattened = ((original_c * row_index) + column_index)
                target_r = flattened // c
                target_c = flattened % c
                new_list[target_r][target_c] = num
        return new_list
