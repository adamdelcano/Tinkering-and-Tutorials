# for https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, string: str) -> int:
        """ Implement atoi which converts a string to an integer.
        The function first discards as many whitespace characters as necessary
        until the first non-whitespace character is found. Then, starting from
        this character, takes an optional initial plus or minus sign followed
        by as many numerical digits as possible, and interprets them as a
        numerical value.
        The string can contain additional characters after those that form the
        integral number, which are ignored and have no effect on the behavior
        of this function. If the first sequence of non-whitespace characters
        in str is not a valid integral number, or if no such sequence exists
        because either str is empty or it contains only whitespace characters,
        no conversion is performed. If no valid conversion could be performed,
        a zero value is returned. """
        initial_index = False  # no starting index yet
        substring = ''  # track substring
        for index, char in enumerate(string):
            # ignore whitespace characters before non-whitespace is found
            if char == ' ' and initial_index is False:
                pass  # continue funtionally the same here I think?
            # first non-whitespace character found!
            elif char != ' ' and initial_index is False:
                try:
                    int(char)
                except ValueError:
                    if char == '-':
                        pass
                    elif char == '+':
                        pass
                    else:
                        return 0
                initial_index = index
            # now go until you hit something not an integer
            else:
                try:
                    int(char)
                except ValueError:
                    # then slice from initial_index to that point
                    substring = string[initial_index:index]
                    break
        # if string ends in an integer make the slice
        if substring == '' and initial_index is not False:
            substring = string[initial_index:]
        # if the string was just all whitespace or something
        elif substring == '' and initial_index is False:
            return 0
        # now to keep it within the bounds it's asking for
        try:
            # This is the unreadable but pleasing one-liner
            # return min((2**31 - 1), max(-2**31, int(substring)))
            substring = int(substring)
        except ValueError:  # sometimes the string is '+' and we gotta deal
            return 0
        if substring > 2**31 - 1:  # upper bound check
            return 2**31 - 1
        elif substring < -2**31:  # lower bound check
            return -2**31
        else:
            return substring  # the finish line
