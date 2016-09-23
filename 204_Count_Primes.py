class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0

        res = [True] * n
        res[0] = False
        res[1] = False

        num = 2

        while num < n:
            if not res[num]:
                num += 1
                continue
            temp = 2
            while num * temp < n:
                res[ num * temp] = False
                temp += 1

            num += 1

        return sum(res)
