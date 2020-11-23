# for https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """Given a string s, find the longest palindromic substring in s."""
        # if it's an empty string skip everything
        if not s:
            return s
        # keep dict of letters with list of indices as value
        letter_dict = {}
        # track longest palindrome, initialize as first letter b/c why not
        longest = s[0]
        # loop over string
        for index, letter in enumerate(s):
            # check previous places letter showed up in string
            prev_places = letter_dict.get(letter)
            if prev_places is not None:
                # check each slice from previous letter to this one
                for prev_index in prev_places:
                    sub_s = s[prev_index:index + 1]
                    # is it a palindrome?
                    if sub_s == sub_s[::-1]:
                        # if longer update
                        if len(sub_s) > len(longest):
                            longest = sub_s
                        # once we find a palindrome all others will be shorter
                        # so we can stop looking at them
                        break
                # add to the indexes to check against
                letter_dict[letter].append(index)
            # if not in the dict then now it is, amazing
            else:
                letter_dict[letter] = [index]
        return longest
