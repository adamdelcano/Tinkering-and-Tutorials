class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solutions = []
        for i, j in enumerate(nums):
            if (target - j) in [b for a, b in enumerate(nums) if a != i]:
                solutions.append(i)
        return solutions