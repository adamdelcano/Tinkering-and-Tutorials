# for https://leetcode.com/problems/regular-expression-matching/


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """ Given an input string (s) and a pattern (p), implement regular
        expression matching with support for '.' and '*'.
        '.' Matches any single character.
        '*' Matches zero or more of the preceding element.
        The matching should cover the entire input string (not partial)."""
        # Track current furthest matching checked index in input string s
        s_index = 0
        # Dict of starting points and truth values. If the s[-1] is in it and
        # True at the end of the process then it's a match
        valid_paths = {-1: True}        
        # I believe assigning this as a variable is worth mem cost vs speed
        s_end = len(s)
        # loop through the pattern matching string
        for index, letter in enumerate(p):
            # if it starts with * we can skip
            if letter == '*':
                continue
            # check for next as *, I am garbage and using try/except instead
            # of if/elif because I thiiink it's quicker? It will throw except
            # exactly once per p, which isn't too bad.
            try:
                if p[index + 1] == '*':
                    any_num_flag = True
                else:
                    any_num_flag = False
            except IndexError:
                any_num_flag = False
            # we're going to check against every valid path because
            # backtracking is more annoying and there are at least
            # edge cases where this could hypothetically be cool
            if any_num_flag is False:
                for path in valid_paths:
                    if path is True and path + 1 < s_end:
                        if letter in (s[path + 1], '.'):
                            valid_paths[path + 1] = True
                        else:
                            valid_paths[path + 1] = False
                

            # if the * flag is up, we update the furthest checked s_index
            # but not starting_points because that's the whole point of it.
            elif any_num_flag is True:
                while s_index <= s_end and letter in (s[s_index], '.'):
                    s_index += 1
        # if we've made it to the end without failing match, it's correct IF
        # the pattern didn't run out before the string
        if s_index > s_end:
            return True
        else:
            return False
