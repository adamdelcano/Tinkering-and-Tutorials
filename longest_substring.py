# for https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Given a string, find the length of the longest substring without
        repeating characters."""
        longest_substring = 0
        current_substring = 0
        # Store used characters as dict keys with their index for value
        previous_characters = {}
        # This speeds things up by letting us skip to next relevant section
        next_starting_point = 0
        # Loop over string. I only use the index, might want to change it?
        for main_index, main_loop_character in enumerate(s):
            # Skip until next starting point
            if main_index < next_starting_point:
                continue
            # Loop over slice of string starting with current position
            for nested_index, character in enumerate(s[index:]):
                # On finding a repeat, set new starting point to right after
                # the character that got repeated (eg. if dv...d -> start at v)
                # Then collect current substring length, reset substring and
                # character dict and break out of nested loop.
                if character in previous_characters:
                    next_starting_point = previous_characters[character] + 1
                    longest_substring = max(
                        current_substring, longest_substring
                    )
                    previous_characters = {}
                    current_substring = 0
                    break
                # If character isn't repeat add it to the dict and increment
                # the count up by one.
                else:
                    previous_characters[character] = nested_index
                    current_substring += 1
        # Collect final substring
        longest_substring = max(current_substring, longest_substring)
        return longest_substring
