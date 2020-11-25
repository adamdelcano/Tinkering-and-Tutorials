# for https://leetcode.com/problems/integer-to-roman/

class Solution:
    def intToRoman(self, num: int) -> str:
        """
        Converts integers to Roman numerals.

        Roman numerals are represented by seven different symbols:
        Symbol       Value
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000
        For example, 2 is written as II in Roman numeral, just two one's added
        together. 12 is written as XII, which is simply X + II. The number 27
        is written as XXVII, which is XX + V + II.

        Roman numerals are usually written largest to smallest from left to
        right. However, the numeral for four is not IIII. Instead, the number
        four is written as IV. Because the one is before the five we subtract
        it making four. The same principle applies to the number nine, which is
        written as IX. There are six instances where subtraction is used:

        I can be placed before V (5) and X (10) to make 4 and 9.
        X can be placed before L (50) and C (100) to make 40 and 90.
        C can be placed before D (500) and M (1000) to make 400 and 900.
        Given an integer, convert it to a roman numeral.

        Takes exactly one parameter, an int, and returns a string.
        """
        # This solution takes advantage of dicts guaranteeing order of insert,
        # which relies on new python- older python would require an
        # ordered_dic which would need to be imported from collections, or use
        # a list of tuples
        roman_numerals = {
            'M': 1000,
            'CM': 900,  # More efficient than handling them in loop I think?
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1
        }
        results = []  # this could be a string, unsure which is more efficient
        for digit in roman_numerals:
            current_num = num // roman_numerals[digit]  # how many of this one
            next_num = num % roman_numerals[digit]  # leftovers
            results.append((digit * current_num))   # add that many of digit
            num = next_num
        return ''.join(results)
