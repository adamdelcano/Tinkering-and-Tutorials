
class Solution:
    def isValid(self, s: str) -> bool:
        valid_chars = '([{'
        if len(s) == 0:
            return True
        if s[-1:] in valid_chars:
            return False
        next_valid = ''
        for letter in s:
            if not (next_valid.endswith(letter) or (letter in valid_chars)):
                return False
            elif letter == '(':
                next_valid += ')'
            elif letter == '[':
                next_valid += ']'
            elif letter == '{':
                next_valid += '}'
            else:
                next_valid = next_valid[:-1]
        if next_valid == '':
            return True
        else:
            return False
