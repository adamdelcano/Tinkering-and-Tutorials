# for https://leetcode.com/problems/container-with-most-water/
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """Given n non-negative integers a1, a2, ..., an , where each
        represents a point at coordinate (i, ai). n vertical lines are drawn
        such that the two endpoints of line i is at (i, ai) and (i, 0). Find
        two lines, which together with x-axis forms a container, such that the
        container contains the most water.
        Note: You may not slant the container and n is at least 2."""

        # for the purposes of trying to get this in one pass
        # establish the longest possible container and initialize
        # with that
        if height[0] >= height[-1]:
            tall_wall = {"index": 0, "size": height[0]}
            short_wall = {"index": (len(height) - 1), "size": height[-1]}
            biggest_area = short_wall["index"] * short_wall["size"]
        else:
            tall_wall = {"index": (len(height) - 1), "size": height[-1]}
            short_wall = {"index": 0, "size": height[0]}
            biggest_area = tall_wall["index"] * short_wall["size"]
        print(biggest_area)  # i'm lazy about debugging
        for index, wall in enumerate(height):
            # don't look below here lol it's so bad
            # I need to completely redo this whole section to have a sane
            # basis for comparison, and a not jumbled-up control flow.
            # This is mid-work, I just ran out of time before nightly walk
            # and I'm starting to get a bit fuzzy and I wanted to document.
            # The theory is that I want to only care about walls that are
            # taller than the initial short wall, and I thought this would
            # be true for the current short wall but I need to reevaluate
            # based on testing. 
            if wall > short_wall["size"]: 
                area = min(
                    tall_wall["size"], wall
                ) * abs(index - tall_wall["index"])
                # also lazy about debugging
                print(f'{area} between {wall},{index} and {tall_wall}')
                # this segment is a nightmare and wrong
                if area > biggest_area:
                    if wall > tall_wall["size"]:
                        short_wall = tall_wall
                        tall_wall = {"index": index, "size": wall}
                    else:
                        short_wall = {"index": index, "size": wall}
                    biggest_area = area
        return biggest_area
