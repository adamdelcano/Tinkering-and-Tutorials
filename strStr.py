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
            # check if letter is in chunk, flag as useless if not
            for chunk in possible_chunks:
                if chunk[1] == target:
                    return chunk[0]
                if chunk[2] is False:
                    continue
                if letter == needle[chunk[1]]:
                    chunk[1] += 1
                else:
                    chunk[2] = False
            # If it's the start of needle, adds a chunk to start tracking
            if letter == needle[0]:
                chunk = [current_haystack_index, 1, True]
                # Second check to catch last character in haystack
                if chunk[1] == target:
                    return chunk[0]
                possible_chunks.append(chunk)
            current_haystack_index += 1

        return -1
