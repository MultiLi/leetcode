# Implement pow(x, n)

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        Solve it recursively.
        """
        isPos = True

        if not n:
            return 1

        if n < 0:
            isPos = False
            n = -n

        if n <= 10:
            res = 1
            for i in range(n):
                res *= x
            if not isPos:
                res =  1 / res
            return res

        l = 1
        div = 10
        while n / div:
            l += 1
            div *= 10

        div = self.myPow(10, l / 2)

        res = self.myPow(self.myPow(x, n / div), div)
        res *= self.myPow(x, n % div)

        if not isPos:
            res = 1 / res

        return res
