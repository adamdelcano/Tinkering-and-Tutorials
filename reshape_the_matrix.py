# for https://leetcode.com/problems/reshape-the-matrix/
from typing import List


class Solution:
    """ Implements matlab's reshape function: given a matrix nums, reshapes it
    into a different size of r row_sizes and c col_sizes while maintaining the
    elements in row_size-traversing order. If imposible returns orig. """
    def matrixReshape(
        self, nums: List[List[int]], row_size: int, col_size: int
    ) -> List[List[int]]:
        # we might be able to ditch these at the cost of some readability
        orig_row_size = len(nums)
        orig_col_size = len(nums[0])
        # check if it can be reshaped
        if (orig_row_size * orig_col_size) != (row_size * col_size):
            return nums
        # We don't use the rows b/c namespace is fucking with me here
        # but it seemed more idiomatic than the other thing that would
        # work: for index in range(row_size)
        for index, row in enumerate(nums):
            next_index = index + 1
            # If this row is too small
            while len(nums[index]) < col_size:
                try:
                    # so these parts are gross and I don't know how to best
                    # manage "keep it under 80 chars", "keep variable names
                    # descriptive", and "keep it not hideous", I hope this
                    # is not the worst compromise.
                    # First take a slice off the next row and add it to
                    # the existing one.
                    nums[
                        index
                    ] += nums[next_index][:(col_size - orig_col_size)]
                    # Then remove that slice from the next row.
                    nums[
                        next_index
                    ] = nums[next_index][(col_size - orig_col_size):]
                    # The next row is empty, we have to go further
                    if len(nums[next_index]) == 0:
                        next_index += 1
                # When there's nothing left, we can stop and return it.
                except IndexError:
                    return nums[:row_size]
            # if the row is too big
            while len(nums[index]) > col_size:
                try:
                    # using new variable because we sometimes get rows bigger
                    # than original_col_size by virtue of adding shit to the 
                    # next row.
                    init_size = len(nums[index])
                    # again sorry that this is a gross statement to read
                    # adding everything past col_size to the next index
                    nums[
                        index + 1
                    ] = nums[index][-(init_size - col_size):] + nums[index + 1]
                    # then removing it from current one
                    nums[index] = nums[index][:-(init_size - col_size)]
                # if we are at the end, we can just pop the end off and append
                # a correctly sized slice, and then the rest. It might be worth
                # doing a fancier version that just takes this essentially
                # flattened mini-list and appends every slice in one step? Idk
                except IndexError:
                    end_of_nums = nums.pop()
                    nums.append(end_of_nums[:col_size])
                    nums.append(end_of_nums[col_size:])
        # and finish
        return nums[:row_size]
