# for https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        valid_chars = {'(': ')', '[': ']', '{': '}'}
        next_character = []
        for character in s:
            if character in valid_chars:
                next_character.append(valid_chars[character])
            elif not next_character or character != next_character.pop():
                return False
        if next_character:
            return False
        else:
            return True
