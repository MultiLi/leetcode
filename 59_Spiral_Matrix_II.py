class Solution(object):
    """
    Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

    For example,
    Given n = 3,

    You should return the following matrix:
    [
        [ 1, 2, 3 ],
        [ 8, 9, 4 ],
        [ 7, 6, 5 ]
    ]
    """
    
    def generateSeq(self, n, dir, origin):
        step = 1 if dir < 2 else -1
        if dir % 2:
            return [(origin[0] + i * step, origin[1]) for i in range(1, n + 1)]
        else:
            return [(origin[0], origin[1] + i * step) for i in range(1, n + 1)]

    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []

        result = [[0 for dummy_i in range(n)] for dummy_j in range(n)]
        origin = (0,-1)
        dummy = origin
        l = n
        dir = 0
        num = 0
        for dummy in self.generateSeq(l, dir, origin):
            num += 1
            result[dummy[0]][dummy[1]] = num
        origin = dummy
        l -= 1
        dir += 1

        while l:
            for d in range(2):
                for dummy in self.generateSeq(l, dir % 4, origin):
                    num += 1
                    result[dummy[0]][dummy[1]] = num
                origin = dummy
                dir += 1
            l -= 1

        return result
