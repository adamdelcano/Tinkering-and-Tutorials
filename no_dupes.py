# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """Given a sorted array nums, remove the duplicates in-place such that
        each element appear only once and return the new length."""
        last_unique = float('-inf')  # Is there a more idiomatic way?
        index_to_change = 0
        for num in nums:
            if num > last_unique:
                last_unique = num
                nums[index_to_change] = last_unique
                index_to_change += 1
        return index_to_change
