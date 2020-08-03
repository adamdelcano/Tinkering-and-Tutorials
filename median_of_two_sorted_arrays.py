# for https://leetcode.com/problems/median-of-two-sorted-arrays
from typing import List


def pop_with_default(target: List) -> int:
    """ Given a list, runs pop and returns None on IndexError. 
    More generalized version should maybe have index=None and default=None
    so that it can be used for more than just this. """
    try:
        return target.pop()
    except IndexError:
        return None


class Solution:
    """Finds the median of two non-empty sorted arrays of size m and n in
    runtime complexity O(log(m + n))."""
    def findMedianSortedArrays(
        self, nums_1: List[int], nums_2: List[int]
    ) -> float:
        # Set up point where median will be
        halfway = (len(nums_1) + len(nums_2)) / 2
        # Initialize num_1 and num_2 and main_list
        num_1 = pop_with_default(nums_1)
        num_2 = pop_with_default(nums_2)
        main_list = []  # Could hypothetically implement counter and not store
        # Loop to populate main_list from arrays
        while len(main_list) <= halfway:  # Don't go further than needed
            # check for empty lists
            if num_1 is not None and num_2 is None:
                main_list.append(num_1)
                num_1 = pop_with_default(nums_1)
            elif num_1 is None and num_2 is not None:
                main_list.append(num_2)
                num_2 = pop_with_default(nums_2)
            elif num_1 >= num_2:
                main_list.append(num_1)
                num_1 = pop_with_default(nums_1)
            elif num_2 > num_1:
                main_list.append(num_2)
                num_2 = pop_with_default(nums_2)
        # Check whether last or average of last two needed, return that
        if halfway % 1 == 0:
            return ((main_list.pop() + main_list.pop()) / 2)
        else:
            return main_list.pop()
