# for https://leetcode.com/problems/implement-strstr/

# note that I'm choosing not to use the obvious solution since well
#        if needle in haystack:
#            return haystack.index(needle)
#        else:
#            return -1


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle or needle == haystack:
            return 0
        target = len(needle)
        possible_chunks = []
        needle_index = 0
        current_haystack_index = 0

        for letter in haystack:
            if haystack[
                current_haystack_index:(current_haystack_index + target)
            ] == needle:
                return current_haystack_index
            current_haystack_index += 1
        return -1
