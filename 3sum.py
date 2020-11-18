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
        triplets = set()  # Container for our solution, set lets us cut dupes
        nums.sort()  # Sorting this allows for optimization
        # We also don't need to check anything bigger than min * -1 because it
        # can't result in zero, since again, sorted list.
        num_dict = {}
        # I tried a dict comprehension: 
        # num_dict = {num:nums.count(num) for num in nums}
        # but it was slower than the loop
        for index, num in enumerate(nums):
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1
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
                # same skipping over checked stuff here
                if second_num <= second_min:
                    continue
                if second_num > max_num:
                    break
                else:
                    second_min = second_num
                # given x + y + z = 0, and knowing x and y, we know z
                third_num = -1 * (num + second_num)
                # dict lookup followed by check that we're not using
                # an item in the list as a match with itself
                if third_num in num_dict:
                    matches = 0
                    if num == third_num:
                        matches += 1
                    if second_num == third_num:
                        matches += 1
                    if num_dict[third_num] > matches:
                        # making this a sorted tuple means we can skip
                        # duplicate entries. 
                        triplets.add(
                            tuple(sorted((num, second_num, third_num)))
                        )
        # then convert it into a list, ta-da
        return list(triplets)
