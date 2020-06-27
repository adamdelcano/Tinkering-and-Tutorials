# for https://leetcode.com/problems/reshape-the-matrix/
from typing import List


class Solution:
    """ Implements matlab's reshape function: given a matrix nums, reshapes it
    into a different size of r rows and c columns while maintaining the
    elements in row-traversing order. If imposible returns original. """
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(nums) * len(nums[0]) != (r * c):  # check if reshaping possible
            return nums  # return if not
        # I don't want to admit how long it took me fumbling before just
        # looking up the list flattening comprehension.
        nums = [digit for row in nums for digit in row]
        # Enumerate lets me have an incrementing counter
        for index, item in enumerate(nums):
            # Convert a column-sized slice of nums into one column
            nums[index:(c + index)] = [nums[index:(c + index)]]
            # Stop when at breakpoint
            if index == r:
                break
        return nums
