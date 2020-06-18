# for https://leetcode.com/problems/reshape-the-matrix/
from typing import List


class Solution:
    """ Implements matlab's reshape function: given a matrix nums, reshapes it
    into a different size of r rows and c columns while maintaining the
    elements in row-traversing order. If imposible returns original. """
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        elements = []  # will hold nums' elements
        step = 0  # lets us keep track of place in elements
        for row in nums:  # flatten nums into elements
            elements.extend(row)
        if len(elements) != (r * c):  # check if reshaping possible
            return nums  # return original if not
        while r > 0:  # might be better to do enumerate here?
            # Actual loop is super simple, just convert that slice into list
            elements[step:(c + step)] = [elements[step:(c + step)]]
            step += 1  # we converted a whole slice into 1 element so only +1
            r -= 1  # decrement r
        return elements
