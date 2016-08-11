# Given n, how many structurally unique BST's (binary search trees) that store
# values 1...n?
#
# For example,
# Given n = 3, there are a total of 5 unique BST's.
#
#   1         3     3      2      1
#    \       /     /      / \      \
#     3     2     1      1   3      2
#    /     /       \                 \
#  2     1         2                 3

class Solution(object):

    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 0: return 0
        if n <= 2: return n

        res = [0] * ( n + 1)
        res[0] = 1
        for i in range(1, n + 1):
            res[i] = 0
            for t in range( i / 2):
                res[i] += 2 * res[t] * res[i - t - 1]
            if i % 2:
                res[i] += res[ (i-1)/2] *res[(i-1)/2]

        return res[n]
