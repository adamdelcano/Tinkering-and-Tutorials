# for https://leetcode.com/problems/greatest-common-divisor-of-strings/


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """Finds the largest string that can be multiplied to completely
        produce the two strings given as arguments."""
        divisor = []  # One list more efficient than new string every loop
        common_divisor = ''  # But then I do this so
        for letter in min(str1, str2):
            divisor.append(letter)
            if len(str1) % len(divisor) == 0 and len(str2) % len(divisor) == 0:
                test_string = ''.join(divisor)
                if (
                    test_string * (len(str1) // len(test_string)) == str1 and
                    test_string * (len(str2) // len(test_string)) == str2
                ):
                    common_divisor = test_string
            else:
                pass
        return common_divisor
