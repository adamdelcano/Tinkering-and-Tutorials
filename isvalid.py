# for https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        valid_chars = {'(': ')', '[': ']', '{': '}'}
        next_letter = []
        for letter in s:
            if letter in valid_chars:
                next_letter.append(valid_chars[letter])
            elif not next_letter:
                return False
            elif letter != next_letter.pop():
                return False
        if next_letter:
            return False
        else:
            return True
