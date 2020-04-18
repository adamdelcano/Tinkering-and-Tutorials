#!/usr/bin/python3


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previously_checked = {}
        for index, num in enumerate(nums):
            desired_num = target - num
            if desired_num in previously_checked:
                return [previously_checked[desired_num], index]
            previously_checked[num] = index
