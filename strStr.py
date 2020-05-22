# for https://leetcode.com/problems/implement-strstr/

# note that I'm choosing not to use the obvious solution since well
#        if needle in haystack:
#            return haystack.index(needle)
#        else:
#            return -1


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # input validation
        if not needle or needle == haystack:
            return 0
        # this is prob unnecessary but I think it's better than
        # having it do them inside the loop?
        needle_len = len(needle)
        haystack_len = len(haystack)
        # single character comparison
        for index, letter in enumerate(haystack):
            if (index + needle_len) > haystack_len:
                break
            if letter == needle[0]:
                for needle_index, needle_letter in enumerate(needle):
                    if haystack[index + needle_index] != needle_letter:
                        break
                else:
                    return index

        return -1
