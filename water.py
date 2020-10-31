# for https://leetcode.com/problems/container-with-most-water/
from typing import List
# PROBLEM DEFINITION
# Given n non-negative integers a1, a2, ..., an , where each
# represents a point at coordinate (i, ai). n vertical lines are drawn
# such that the two endpoints of line i is at (i, ai) and (i, 0). Find
# two lines, which together with x-axis forms a container, such that the
# container contains the most water.
# Note: You may not slant the container and n is at least 2."""


class Wall():
    """
    Notional wall of a possible container in an array of walls.

    Wall object makes this problem more readable than list or tuple
    but could easily have been a dict with 'height' and 'position', and
    just duplicated the code the few times it would have come up. Checking on
    leetcode, neither option is dramatically more performant for this use case,
    but it's likely dict beats it in most use cases.

    T
    """

    def __init__(self, position: int, height_list: List) -> None:
        """
        Initializes the wall with index and the list it's using, and gets
        height from that.
        """
        self.position = position
        self.height_list = height_list
        self.height = height_list[position]

    def move(self, direction) -> None:
        """
        Moves the wall and recalculates height.

        If given another wall, it will move to that wall's location,
        otherwise it will just increment it's position by the amount given.
        It then recalculates height either by referencing the other wall or
        the original list.
        """
        if type(direction) is Wall:
            self.position = direction.position
            self.height = direction.height
        else:
            self.position += direction
            self.height = self.height_list[self.position]


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
            distance = abs(first_wall.position - second_wall.position)
            shorter_wall = min(first_wall.height, second_wall.height)
            return distance * shorter_wall

        left_wall = Wall(0, height)
        left_cursor = Wall(0, height)
        right_wall = Wall((len(height) - 1), height)
        right_cursor = Wall((len(height) - 1), height)
        max_area = wall_area(left_wall, right_wall)
        while left_cursor.position != right_cursor.position:
            if left_wall.height <= right_wall.height:
                left_cursor.move(1)
                if left_cursor.height > left_wall.height:
                    left_wall.move(left_cursor)
                    area = wall_area(left_wall, right_wall)
                    max_area = max(area, max_area)
            else:
                right_cursor.move(-1)
                if right_cursor.height > right_wall.height:
                    right_wall.move(right_cursor)
                    area = wall_area(left_wall, right_wall)
                    max_area = max(area, max_area)

        return max_area
