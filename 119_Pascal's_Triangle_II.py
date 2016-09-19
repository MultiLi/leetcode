# Directly define n-choose-k operation.

class Solution(object):
    def nck(self,n,k):
        k = min(k, n-k)

        up = 1
        down = 1

        ind = n
        start = 1
        while ind > n - k:
            up *= ind
            down *= start
            start += 1
            ind -= 1
        print up, down
        return up/down

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        res = []
        for i in range(rowIndex + 1):
            res.append(self.nck(rowIndex, i))

        return res
