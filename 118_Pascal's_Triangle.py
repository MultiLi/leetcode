class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        if not numRows:
            return []

        res = [[1]]

        if numRows == 1:
            return res

        depth = 1

        while depth < numRows:
            res.append([0]* (depth + 1))

            res[-1][0] = res[-2][0]
            res[-1][-1] = res[-2][-1]
            for i in range(1,depth):
                res[-1][i] = res[-2][i-1] + res[-2][i]

            depth += 1

        return res
