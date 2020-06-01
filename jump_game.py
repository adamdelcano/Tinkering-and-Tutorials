# for https://leetcode.com/problems/jump-game/


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """Given an array of non-negative integers, you are initially
        positioned at the first index of the array. Each element in the
        array represents your maximum jump length at that position.
        Determine if you are able to reach the last index."""
        furthest = 0
        # index of last object will be len(nums) - 1 and that's actual target
        last = len(nums) - 1
        for index, num in enumerate(nums):
            # If you can get there you can stop checking YOU WIN
            if furthest >= last:
                return True
            # If you're past where you could go GAME OVER and you can stop now
            if furthest < index:
                return False
            # Update furthest jump with furthest you can jump from here
            furthest = max(furthest, (index + num))
