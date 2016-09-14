# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
# of rows like this: (you may want to display this pattern in a fixed font for
# better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a
# number of rows:
#
# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if not s:
            return str('')

        if numRows == 1:
            return s

        res = []

        i = 0
        ns = numRows - 1

        while ns >= 0:
            j = i
            step = ns
            while j < len(s):
                if step:
                    res.append(s[j])
                    j += 2 * step
                step = numRows - 1 - step
            ns -= 1
            i += 1

        return ''.join(res)
