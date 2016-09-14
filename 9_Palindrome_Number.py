# Judging if the given input integer is a palindrome number without using extra
# space.
# The problem here is all negative integers are not palindrome

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        exp = 0
        n = 1
        while x / n:
            n *= 10
            exp += 1

        n /= 10
        divider = n

        while exp > 1:
            if x / divider != x % ( n / divider * 10) / ( n / divider):
                return False
            x -= x/divider * divider
            divider /= 10
            exp -= 2

        return True
