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
        if not nums:   # sanitization
            return []
        triplets = []  # Container for our solution
        nums.sort()  # Sorting this allows for optimization
        num_reverse = [i for i in reversed(nums)]  # I'm not proud
        num_set = set(nums)  # I cannot emphasize enough how not proud I am
        # Since the list is now sorted, we don't ever need to check numbers
        # as small or smaller than ones we've checked already - we will have
        # found all unique triplets for them already.
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
                # update bounds
                min_num = num
                max_num = -1 * num
                second_min = min_num - 1  # same rationale for the inner loop
            for second_index, second_num in enumerate(nums[index + 1:]):
                if second_num <= second_min:
                    continue
                if second_num > max_num:
                    break
                else:
                    second_min = second_num
                # given x + y + z = 0, and knowing x and y, we know z
                third_num = -1 * (num + second_num)
                # for very large lists the set check does a lot of work
                if third_num in num_set:
                    #  This next line seems like there has to be a better way
                    if third_num in num_reverse[:-2 - (index + second_index)]:
                        threesum = [num, second_num, third_num]
                        triplets.append(threesum)
        return triplets
