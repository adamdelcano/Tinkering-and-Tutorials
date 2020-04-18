class Solution:
    def isValid(self, s: str) -> bool:
        valid_chars = {'(': ')', '[' : ']', '{': '}'}
        next_valid = ''
        for letter in s:
            if letter in valid_chars:
                next_valid += valid_chars[letter]
            elif not next_valid.endswith(letter):
                return False
            else:
                next_valid = next_valid[:-1]
        if next_valid == '':
            return True
        else:
            return False
