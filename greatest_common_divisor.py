# for https://leetcode.com/problems/greatest-common-divisor-of-strings/


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """Finds the largest string that can be multiplied to completely
        produce the two strings given as arguments."""
        divisor = []  # One list more efficient than new string every loop
        common_divisor = ''  # But then I do this so
        for letter in str1:
            divisor.append(letter)
            test_string = ''.join(divisor)
            if (
                len(test_string) <= len(str1) and
                len(test_string) <= len(str2) and
                test_string * (len(str1) // len(test_string)) == str1 and
                test_string * (len(str2) // len(test_string)) == str2
            ):  # Probably not the most efficient way to check these, sorry.
                common_divisor = test_string
        return common_divisor
