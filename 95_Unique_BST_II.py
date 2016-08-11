# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Given an integer n, generate all structurally unique BST's (binary search
# trees) that store values 1...n.
#
# For example,
# Given n = 3, your program should return all 5 unique BST's shown below.
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
        Similar to the solution to Prob. 96, the only difference is the result
        value is an array.
        """
        if n == 0: return [1]

        res = [0] * ( n + 1)
        res[0] = 1
        for i in range(1, n + 1):
            res[i] = 0
            for t in range( i / 2):
                res[i] += 2 * res[t] * res[i - t - 1]
            if i % 2:
                res[i] += res[ (i-1)/2] *res[(i-1)/2]

        return res

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        Iteratively build the BST bottom-up.
        In dictionary, a key (start, size) corresponds to a list of BSTs
        composed of range(start,size) nodes.
        I beat more than 90 percent programmers in this problem! Cool!
        """
        if not n: return []
        if n == 1: return [TreeNode(1)]

        numMap = self.numTrees(n)

        subMap = {}

        for i in range(n):
            subMap[(i, 1)] = [TreeNode(i + 1)]
            subMap[(i, 0)] = [None]

        subMap[(n,0)] = [None]

        for size in range(2, n + 1):
            start = 0
            while start + size < n + 1:
                roots = [None] * numMap[size]
                tind = 0
                for root in range(start, start + size):
                    lsize = root - start
                    lefts = subMap[(start, lsize)]
                    rights = subMap[(root + 1, size - lsize - 1)]
                    tsize = ( numMap[lsize], numMap[size - lsize - 1] )
                    for left in lefts:
                        for right in rights:
                            roots[tind] = TreeNode(root + 1)
                            roots[tind].left = left
                            roots[tind].right = right
                            tind += 1
                subMap[(start, size)] = roots
                start += 1

        return subMap[(0,n)]
