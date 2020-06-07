# for https://leetcode.com/problems/median-of-two-sorted-arrays
from typing import List


class Solution:
    """Finds the median of two non-empty sorted arrays of size m and n in
    runtime complexity O(log(m + n)). Not finished."""
    def findMedianSortedArrays(
        self, nums1: List[int], nums2: List[int]
    ) -> float:

        mainlist = sorted(nums1 + nums2)
        halfway = len(mainlist) // 2
        if len(mainlist) % 2 == 0:
            median = (mainlist[halfway] + mainlist[halfway - 1]) / 2
            return median
        else:
            return mainlist[halfway]
