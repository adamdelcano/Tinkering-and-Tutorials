# for https://leetcode.com/problems/plus-one/
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """Given a non-empty list representing a non-negative integer,
        adds 1 to the integer, while maintaining the list form, and
        not cheating by turning it into a concatenated string, changing
        the string into an integer, adding 1 to that, and reversing
        the process, which frankly wasn't even meaningfully slower."""
        zeroes_to_append = 0
        new_digit = digits.pop() + 1
        if new_digit < 10:
            digits.append(new_digit)
        else:  # if [9, 9, ... 9] there's a chain reaction that needs to happen
            zeroes_to_append += 1
            while digits:
                new_digit = digits.pop() + 1
                if new_digit < 10:
                    digits.append(new_digit)
                    break  # Stops once there's not a 9 at the end
                else:
                    zeroes_to_append += 1
            if not digits:
                digits = [1]  # If it 999 it's empty now so start at 1
            while zeroes_to_append > 0:  # replace every 9 we removed with a 0
                digits.append(0)
                zeroes_to_append -= 1
        return digits
