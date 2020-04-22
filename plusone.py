# for https://leetcode.com/problems/plus-one/
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        '''Given a non-empty list representing a non-negative integer,
        adds 1 to the integer, while maintaining the list form, and
        not cheating by turning it into a concatenated string, changing
        the string into an integer, adding 1 to that, and reversing
        the process, which frankly wasn't even meaningfully slower.'''

        counter = 0
        new_digit = digits.pop() + 1
        if new_digit < 10:
            digits.append(new_digit)
        else:
            counter += 1
            while digits:
                new_digit = digits.pop() + 1
                if new_digit < 10:
                    digits.append(new_digit)
                    break
                else:
                    counter += 1
                    continue
            if not digits:
                digits = [1]
            while counter > 0:
                digits.append(0)
                counter -= 1
        return digits
