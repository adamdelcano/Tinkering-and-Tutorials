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
        i = 0  # this is the integer we'll be constructing
        neg_flag = False  # this could be 1 instead and *= -1 to switch
        int_max = 2**31 - 1
        int_min = -2**31
        started = False
        a = string.lstrip()   # work with a string with removed whitespace
        for char in a:
            # test if char is number, add to i if so
            if char.isnumeric() and i == 0 and started is False:
                i = int(char)
                started = True
            elif char.isnumeric():
                i *= 10
                i += int(char)
            # special case to handle +/-, can be expanded to handle \t, \r, \n
            # using an escape flag and some extra elifs
            elif char.isnumeric() is False and i == 0 and started is False:
                if char == '-':
                    started = True
                    neg_flag = True
                elif char == '+':
                    started = True
                else:
                    return 0
            # now go until you hit something not an integer
            else:
                break
        # if the neg_flag was 1/-1 we could just always i *= neg_flag but I
        # think that opens the door for more unexpected behavior down the line
        # than this conditional
        if neg_flag is True:
            i *= -1
        return min(max(int_min, i), int_max)
