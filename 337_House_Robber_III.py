# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# The thief has found himself a new place for his thievery again. There is only
# one entrance to this area, called the "root." Besides the root, each house has
# one and only one parent house. After a tour, the smart thief realized that
# "all houses in this place forms a binary tree". It will automatically contact
# the police if two directly-linked houses were broken into on the same night.
#
# Determine the maximum amount of money the thief can rob tonight without
# alerting the police.
#
# Example 1:
#     3
#    / \
#   2   3
#    \   \
#     3   1
# Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

class Solution(object):

    def exploreNode(self, root):

        leven,lodd, reven, rodd = 0,0,0,0

        if root.left:
            leven, lodd = self.exploreNode(root.left)

        if root.right:
            reven,rodd = self.exploreNode(root.right)

        return lodd + rodd, max(lodd + rodd, root.val + leven + reven)

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        Since it is a binary tree problem, it's natural to solve it by recursion.
        Divide the max benefit from the robbery of a tree into 2 subproblems,
        namely odd and even, depending on whether the root is contained.

        The implementation of recursion makes this code seems so concise.
        """
        if not root: return 0

        return max(self.exploreNode(root))
