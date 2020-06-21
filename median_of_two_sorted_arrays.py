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
        num_1 = float(-inf)
        num_2 = float(-inf)
        main_list = []  # Could hypothetically implement counter and not store
        # Loop to populate main_list from arrays
        while len(main_list) <= halfway:  # Don't go further than needed
            # Compare num_1, num_2, add larger to list and reset it to -inf
            if num_1 >= num_2:
                if num_1 == float(-inf):  # check if variables initialized
                    pass
                else:
                    main_list.append(num_1)
                    num_1 = float(-inf)
            elif num_2 > num_1:
                main_list.append(num_2)
                num_2 = float(-inf)
            # Pop end off non-empty lists to replace -inf variables
            if num_1 == float(-inf) and nums_1:
                num_1 = nums_1.pop()
            if num_2 == float(-inf) and nums_2:
                num_2 = nums_2.pop()
        # Check whether last or average of last two needed, return that
        if halfway % 1 == 0:
            return ((main_list.pop() + main_list.pop()) / 2)
        else:
            return main_list.pop()
