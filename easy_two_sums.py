class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solutions = []
        for i, j in enumerate(nums):
            if target - j in nums:
                if j == (target/2) and nums.count(j) < 2:
                    pass
                else: solutions.append(i)
        return solutions