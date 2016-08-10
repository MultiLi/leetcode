# Reverse digits of an integer.
#
# Example1: x = 123, return 321
# Example2: x = -123, return -321

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        It's ridiculous to take into account an unexistant problem.
        """

        isPos = True
        if x < 0:
            x = -x
            isPos = False

        res = int(str(x)[::-1]) if int(str(x)[::-1]) <= 1<<31 else 0
        if isPos:
            return res
        else:
            return -1 * res
