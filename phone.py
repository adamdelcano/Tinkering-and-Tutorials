#https://leetcode.com/problems/letter-combinations-of-a-phone-number/
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Given a string containing digits from 2-9 inclusive, return all
        possible letter combinations that the number could represent.
        Return the answer in any order.

        This solution builds a dict of digits keyed to letter combinations,
        then loops over the phone number, for each digit in the phone number
        looping over the letters in it's dict entry, and appending each letter
        to every entry in the total list of possible combinations. It then
        updates the list of possible combinations and moves to the next digit.
        """

        if not digits:
            return []
        digits_dict = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        combinations = ['']
        for digit in digits:
            digit_container = []
            for letter in digits_dict[digit]:
                for combination in combinations:
                    digit_container.append(combination + letter)
            combinations = digit_container
        return combinations
