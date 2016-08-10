# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root
# node down to the farthest leaf node.

class Solution(object):
    def goDown(self, root, depth):
        left, right = 0, 0

        if root.left:
            left = self.goDown(root.left, depth + 1)
        if root.right:
            right = self.goDown(root.right, depth + 1)
        return max(depth, left, right)

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0

        return self.goDown(root, 1)
