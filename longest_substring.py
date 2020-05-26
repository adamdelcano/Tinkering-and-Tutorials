# for https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Given a string, find the length of the longest substring without
        repeating characters."""
        longest_substring = 0
        used_chars = {}
        current_substring = 0
        anchor = 0
        for index, char in enumerate(s):
            # The anchor variable lets us skip useless stuff
            if index < anchor:
                continue
            # I swear there's a way to do this without nested loops
            # but I've been trying all week halfassedly and I think
            # at this point I'm better off submitting and seeing what
            # you folks think. The inner loop is pretty self-explanatory
            # I think- I'm happy with the idea of using dict but it
            # tantalizes me with not resetting it and just doing one loop.
            for check_index, check_char in enumerate(s[index:]):
                if check_char in used_chars:
                    anchor = used_chars[check_char] + 1
                    longest_substring = max(
                        current_substring, longest_substring
                    )
                    used_chars = {}
                    current_substring = 0
                    break
                else:
                    used_chars[check_char] = check_index
                    current_substring += 1
        # Collect final substring
        longest_substring = max(current_substring, longest_substring)
        return longest_substring
