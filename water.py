# for https://leetcode.com/problems/container-with-most-water/
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        biggest_area = 0
        for index, wall in enumerate(height):
            for other_index, other_wall in enumerate(height):
                if other_index <= index:
                    continue
                area = min(wall, other_wall) * (other_index - index)
                if area > biggest_area:
                    biggest_area = area
        return biggest_area
