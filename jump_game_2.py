# for https://leetcode.com/problems/jump-game-ii

from typing import List


class Solution:
    """Given an array of non-negative integers, you are initially positioned
    at the first index of the array. Each element in the array represents
    your maximum jump length at that position. Your goal is to reach the last
    index in the minimum number of jumps. You can assume that you can always
    reach the last index."""
    def jump(self, nums: List[int]) -> int:
        """Loops through the list, considering everything inside the current
        jump as potential choices for the next starting point, then picks the
        furthest jump for group as the starting point for the next one. Each
        time it does this it increments the jumps taken until it hits the
        finish line and adds one more jump."""
        current_jump_ending = 0
        potential_jump_distance = 0
        jumps_taken = 0
        finish_line = len(nums) - 1
        if finish_line == 0:  # This is hacky there might be a better way
            return jumps_taken
        for index, num in enumerate(nums):  # Maybe a while loop instead?
            potential_jump_distance = (
                max(potential_jump_distance, (index + num))
            )
            if potential_jump_distance >= finish_line:
                jumps_taken += 1
                return jumps_taken
            if index == current_jump_ending:
                current_jump_ending = potential_jump_distance
                jumps_taken += 1
