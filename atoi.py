# for https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

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
        stripped_string = string.lstrip()   # remove whitespace
        try:
            # Not sure which version is more readable, have commented one out.
            # They don't seem to make a difference in runtime on leetcode.
            # I kinda assume the first is slightly longer but still an O(1)
            # check so not relevant, just a matter of which looks better to
            # the human eye.
            #
            # if stripped_string[0] in ('+', '-'):
            #     if stripped_string[0] == '-':
            #         neg_flag = True
            #     stripped_string = stripped_string[1:]
            if stripped_string[0] == '-':
                neg_flag = True
                stripped_string = stripped_string[1:]
            elif stripped_string[0] == '+':
                stripped_string = stripped_string[1:]
        except IndexError:
            return 0
        for char in stripped_string:
            # test if char is number, add to i if so
            if char.isnumeric():
                i *= 10
                i += int(char)
            # now go until you hit something not an integer
            else:
                break
        # if the neg_flag was 1/-1 we could just always i *= neg_flag but I
        # think that opens the door for more unexpected behavior down the line
        # than this conditional
        if neg_flag is True:
            i *= -1
        return min(max(self.INT_MIN, i), self.INT_MAX)
