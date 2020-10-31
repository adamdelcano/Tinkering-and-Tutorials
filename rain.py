https://leetcode.com/problems/trapping-rain-water/
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        last_wall = 0
        total_trapped_water = 0
        for wall in height:
            trapped_water = last_wall - wall
            if trapped_water >= 0:
                total_trapped_water += trapped_water
            else:
                last_wall = wall
        return total_trapped_water