# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recu(self, left, right):
        if left.val != right.val:
            return False
        if left.left and right.right:
            if not self.recu(left.left, right.right):
                return False
        elif not (left.left or right.right):
            pass
        else:
            return False

        if left.right and right.left:
            if not self.recu(left.right, right.left):
                return False
        elif not (left.right or right.left):
            pass
        else:
            return False

        return True

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        if root.left and root.right:
            return self.recu(root.left, root.right)
        elif not (root.left or root.right):
            return True
        else:
            return False
