# for https://leetcode.com/problems/count-and-say/

# This is basically the same solution as for stonks2.py
# I didn't directly copy/paste the code since this is about strings not ints
# But I basically could have
# I probably could use fewer pointers but otherwise this seems reasonable?
# Much as leetcode optimization isn't a thing I care about it was faster
# than most of them


class Solution:
    def countAndSay(self, n: int) -> str:
        result = ['1']
        for counted_and_said in range(1, n):
            temp_result = []
            last_char = ''
            freq = 0
            for character in result:
                if character == last_char or last_char == '':
                    freq += 1
                    last_char = character
                else:
                    temp_result.extend([str(freq), last_char])
                    freq = 1
                    last_char = character
            # collect last block
            temp_result.extend([str(freq), last_char])
            result = temp_result
        return ''.join(result)
