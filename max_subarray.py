
# https://leetcode.com/problems/maximum-subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest_sum = float("-inf")
        current_sum = 0
        for num in nums:
            current_sum += num
            current_sum = max(current_sum, num)
            largest_sum = max(current_sum, largest_sum)
        return largest_sum
