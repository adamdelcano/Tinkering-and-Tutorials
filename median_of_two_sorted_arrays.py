# for https://leetcode.com/problems/median-of-two-sorted-arrays
from typing import List


class Solution:
    """Finds the median of two non-empty sorted arrays of size m and n in
    runtime complexity O(log(m + n))."""
    def findMedianSortedArrays(
        self, nums_1: List[int], nums_2: List[int]
    ) -> float:
        # Set up point where median will be
        halfway = (len(nums_1) + len(nums_2)) / 2
        # Initialize num_1 and num_2 and main_list
        try:
            num_1 = nums_1.pop()
        except IndexError:
            num_1 = None
        try:
            num_2 = nums_2.pop()
        except IndexError:
            num_2 = None
        main_list = []  # Could hypothetically implement counter and not store
        # Loop to populate main_list from arrays
        while len(main_list) <= halfway:  # Don't go further than needed
            # check for empty lists
            if num_1 is not None and num_2 is None:
                main_list.append(num_1)
                try:
                    num_1 = nums_1.pop()
                except IndexError:
                    num_1 = None
            elif num_1 is None and num_2 is not None:
                main_list.append(num_2)
                try:
                    num_2 = nums_2.pop()
                except IndexError:
                    num_2 = None
            # now compare
            elif num_1 >= num_2:
                main_list.append(num_1)
                try:
                    num_1 = nums_1.pop()
                except IndexError:
                    num_1 = None
            elif num_2 > num_1:
                main_list.append(num_2)
                try:
                    num_2 = nums_2.pop()
                except IndexError:
                    num_2 = None
        # Check whether last or average of last two needed, return that
        if halfway % 1 == 0:
            return ((main_list.pop() + main_list.pop()) / 2)
        else:
            return main_list.pop()
