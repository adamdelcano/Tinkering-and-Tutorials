class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Finds the unique combinations of 3 elements (triplets)
        that have a sum of 0 in the list.

        Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
        Find all unique triplets in the array which gives the sum of zero.

        Notice that the solution set must not contain duplicate triplets.
        Example 1:
        Input: nums = [-1,0,1,2,-1,-4]
        Output: [[-1,-1,2],[-1,0,1]]

        Example 2:
        Input: nums = []
        Output: []

        Example 3:
        Input: nums = [0]
        Output: []

        Constraints:
        0 <= nums.length <= 3000
        -105 <= nums[i] <= 105
        """
        if not nums or len(nums) < 3:   # sanitization
            return []
        triplets = []
        nums.sort()  # Sorting this lets us use math to think stuff through.
        # We also don't need to check anything bigger than min * -1 because it
        # can't result in zero, since again, sorted list.
        min_num = nums[0] - 1
        max_num = -1 * min_num
        for index, num in enumerate(nums):
            if num <= min_num:
                continue  # skip if at or below lower bound
            elif num >= max_num:
                break  # if we're above upper bound just stop entirely
            else:
                # update lower bound
                min_num = num
            # Trying the cursors at low and high ends of list
            # and using the fact that I can tell which way I need to move
            # to implement a more memory-efficient search without using a dict.
            # It IS slower though. I think outside of showing how I'd do it
            # without one, the dict usually makes more sense?
            # low / high could be left / right
            low = index + 1
            high = len(nums) - 1
            while low < high:
                # check if result is 0, if over 0 move high down, if under 0
                # move low up, if it's 0 add it and then move the cursors
                # appropriately
                result = num + nums[low] + nums[high]
                if result > 0:
                    high -= 1
                elif result < 0:
                    low += 1
                elif result == 0:
                    triplets.append((num, nums[low], nums[high]))
                    # these while loops skip until a unique value
                    while low < high and nums[low] == nums[low + 1]:
                        low += 1
                    low += 1
                    while high > low and nums[high] == nums[high - 1]:
                        high -= 1
                    high -= 1
        return triplets
