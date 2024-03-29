# for https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """Convert string to zig-zagged version. What is zig-zagged?

        The string "PAYPALISHIRING" is written in a zigzag pattern on a given
        number of rows like this: (you may want to display this pattern in a
        fixed font for better legibility)
        example for s: "PAYPALISHIRING" numRows: 3

        P   A   H   N
        A P L S I I G
        Y   I   R

        And then read line by line: "PAHNAPLSIIGYIR"

        Note that as more rows show up the zigs and zags grow too:
        example for s: "PAYPALISHIRING" numRows: 4

        P     I    N
        A   L S  I G
        Y A   H R
        P     I

        This would be "PINALSIGYAHRPI"
        This function takes a string and a number of rows and outputs the
        converted gross final string. """
        # I don't think it's worth figuring out an algorithm that handles
        # the edge case of a single row vs just adding it in
        if numRows == 1:
            return s
        # construct dictionary of rows
        row_dict = {row: '' for row in range(numRows)}
        # current row we're adding to the end of
        current_row = 0
        # this will let us navigate
        direction = 1
        for letter in s:
            # add to current row
            row_dict[current_row] += letter
            # move up or down a row
            current_row += direction
            # if out of bounds, switch direction and go back
            if current_row not in row_dict:
                direction *= -1
                current_row += (2 * direction)
        # voltron the dict back together into a string
        return ''.join(row_dict[row] for row in range(numRows))
