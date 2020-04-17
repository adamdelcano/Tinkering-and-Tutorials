
class Solution:
    def twoSum(self, nums, target):
        solutions = [
            i for i, j in enumerate(nums, 0)
            if j * -1 + target in
            [b for a, b in enumerate(nums) if a != i]]
        return solutions
