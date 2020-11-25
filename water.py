# for https://leetcode.com/problems/container-with-most-water/
from typing import List
# PROBLEM DEFINITION
# Given n non-negative integers a1, a2, ..., an , where each
# represents a point at coordinate (i, ai). n vertical lines are drawn
# such that the two endpoints of line i is at (i, ai) and (i, 0). Find
# two lines, which together with x-axis forms a container, such that the
# container contains the most water.
# Note: You may not slant the container and n is at least 2."""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Calculates max amount of water contained in list of notional pool walls

        This problem is asking you to find the largest value between any two
        numbers in a list, where the value is the distance between their
        indices multiplied by the lower of the numbers. There's a lot of
        fluff trying to describe that and it doesn't read very well off of
        leetcode, but that's what it's actually asking for.

        This function first defines a nested function that actually calculates
        the area between two walls as described. Then it defines the left and
        right walls, as well as cursors on the left and right sides. It
        compares the left/right walls, moves the cursor corresponding to the
        shorter wall one step closer to the middle and updates the cursor's
        values appropriately. If the cursor is now taller than the wall it
        represents, it updates the wall, calculates the area between the
        now-updated walls, and if that's larger than the maximum area found
        so far, updates that. Once the left and right cursors meet, the entire
        list has been searched, and the function returns the max area.
        """
        def wall_area(first_wall, second_wall):
            distance = abs(left_wall['index'] - right_wall['index'])
            shortest = min(left_wall['height'], right_wall['height'])
            return (distance * shortest)
        left_wall = {'index': 0, 'height': height[0]}
        left_cursor = {'index': 0, 'height': height[0]}
        right_wall = {'index': (len(height) - 1), 'height': height[-1]}
        right_cursor = {'index': (len(height) - 1), 'height': height[-1]}
        max_area = wall_area(left_wall, right_wall)
        while left_cursor['index'] != right_cursor['index']:
            if left_wall['height'] <= right_wall['height']:
                left_cursor['index'] += 1
                left_cursor['height'] = height[left_cursor['index']]
                if left_cursor['height'] > left_wall['height']:
                    left_wall['height'] = left_cursor['height']
                    left_wall['index'] = left_cursor['index']
                    area = wall_area(left_wall, right_wall)
                    max_area = max(area, max_area)
            else:
                right_cursor['index'] -= 1
                right_cursor['height'] = height[right_cursor['index']]
                if right_cursor['height'] > right_wall['height']:
                    right_wall['height'] = right_cursor['height']
                    right_wall['index'] = right_cursor['index']
                    area = wall_area(left_wall, right_wall)
                    max_area = max(area, max_area)

        return max_area
