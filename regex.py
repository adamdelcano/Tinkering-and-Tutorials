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
        # Track last non-* match index, since * makes things complicated
        prev_s_index = 0
        # I believe assigning this as a variable is worth mem cost vs speed
        s_end = len(s) - 1
        # loop through the pattern matching string in 2-character slices
        # this lets us check for * without using too much overhead
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
            # if it's a regular character or . we can check simply
            if any_num_flag is False:
                # tuple here lets us check both, fancy
                if letter in (s[s_index], '.'):
                    prev_s_index = s_index
                    s_index += 1
                # check against the last two characters pre-*, this could
                # be one elif with a tuple but each needs different action so
                # diffentiation is worthwhile.
                elif letter == s[prev_s_index]:
                    s_index = prev_s_index + 1
                elif letter == s[prev_s_index + 1]:
                    match = True
                    prev_s_index += 1
                    s_index = prev_s_index + 1
                # Not match? THEN DIE!
                else:
                    print(f'Failure: {letter} did not match {s[s_index]}')
                    print(f'It also didn\'t match {s[prev_s_index]}')
                    print(f'or {s[prev_s_index + 1]}.')
                    return False
            # if the * flag is up, we update the furthest checked s_index
            # but not prev_s_index because that's the whole point of it.
            elif any_num_flag is True:
                while s_index <= s_end and letter in (s[s_index], '.'):
                    s_index += 1
        # if we've made it to the end without failing match, it's correct IF
        # the pattern didn't run out before the string
        if s_index > s_end:
            return True
        else:
            return False
