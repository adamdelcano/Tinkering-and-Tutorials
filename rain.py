# https://leetcode.com/problems/trapping-rain-water/
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Given n non-negative integers representing an elevation map where the
        width of each bar is 1, compute how much water it can trap after
        raining.
        """
        if not height:
            return 0
        left_cursor = {
            "index": -1,
            "max_height": 0,
            "height": 0
        }
        right_cursor = {
            "index": (len(height) - 1),
            "max_height": height[-1],
            "height": height[-1]
        }
        rain = 0
        while left_cursor["index"] != right_cursor["index"]:
            if left_cursor["height"] < right_cursor["height"]:
                left_cursor["index"] += 1
                left_cursor["height"] = height[left_cursor["index"]]
                if left_cursor["height"] > left_cursor["max_height"]:
                    left_cursor["max_height"] = left_cursor["height"]
                elif left_cursor["height"] < right_cursor["max_height"]:
                    rain += (
                        min(
                            left_cursor["max_height"],
                            right_cursor["max_height"]
                        ) - left_cursor["height"]
                    )
            elif right_cursor["height"] <= left_cursor["height"]:
                right_cursor["index"] -= 1
                right_cursor["height"] = height[right_cursor["index"]]
                if right_cursor["height"] > right_cursor["max_height"]:
                    right_cursor["max_height"] = right_cursor["height"]
                elif right_cursor["height"] < left_cursor["max_height"]:
                    rain += (
                        min(
                            left_cursor["max_height"],
                            right_cursor["max_height"]
                        ) - right_cursor["height"]
                    )
        return rain
