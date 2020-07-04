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
        # do this like I did the stocks problems with a container and
        # a condition to reset it
        temp_row = []
        index = 0
        for row in nums:
            temp_row += row
            # once the temporary row is full, dump it
            if len(temp_row) >= c:
                nums[index] = temp_row[:c]
                index += 1
                temp_row = temp_row[c:]
        # if there are more rows in the new matrix temp_row will have
        # stuff in after iterating through, this adds it at the end in
        # column-sized chunks.
        while len(temp_row) >= c:
            nums.append(temp_row[:c])
            temp_row = temp_row[c:]
        # cull the rows past where they were any
        del nums[r:]
        return nums
