# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 1:
            return 1

        low = 1
        high = n

        while True:
            mid = (low + high) / 2
            res = guess(mid)
            if not res:
                return mid
            elif res == 1:
                low = mid + 1
            else:
                high = mid - 1
        
