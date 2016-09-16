# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Recursively judge if the subtree rooted by current node is a balanced binary
# tree, since the balanced binary tree self is recursively defined.

class Solution(object):

    def recur(self, node):
        dleft = 0
        dright = 0
        if node.left:
            dleft = self.recur(node.left)
            if not dleft:
                return 0
        if node.right:
            dright = self.recur(node.right)
            if not dright:
                return 0

        if dleft - dright > 1 or dleft - dright < -1:
            return 0

        return max(dleft, dright) + 1


    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if (not root) or not (root.left or root.right):
            return True

        if self.recur(root):
            return True
        else:
            return False
