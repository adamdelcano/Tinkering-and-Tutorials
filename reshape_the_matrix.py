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
        # if there are more columns in the new rows, can iterate easily
        if c >= original_c:
            # assign correct indices to everything
            for row_index, row in enumerate(nums):
                for column_index, num in enumerate(row):
                    # I EXTREMELY did not think of this math myself
                    flattened = ((original_c * row_index) + column_index)
                    target_r = flattened // c
                    target_c = flattened % c
                    print(target_r, target_c)
                    try:
                        nums[target_r][target_c] = num
                    except IndexError:
                        nums[target_r].append(num)
            # cull nonexistent rows
            del nums[r:]
        # If there are fewer columns, we need to make a container to store
        # numbers that we haven't gotten to yet
        else:
            # create a container list for rows
            current_row = []
            # iterate over nums, collecting until current_row is full then
            # assigning it.
            for index in range(r):
                try:
                    row = current_row + nums[index]
                    current_row = row[c:]
                    row = row[:c]
                    nums[index] = row
                except IndexError:
                    row = current_row[:c]
                    current_row = current_row[c:]
                    nums.append(row)
        return nums
