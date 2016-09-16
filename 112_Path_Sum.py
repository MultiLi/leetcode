# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        stack = [(root, root.val)]

        while stack:
            cnode = stack.pop()
            if not (cnode[0].left or cnode[0].right):
                if cnode[1] == sum:
                    return True

                continue

            if cnode[0].left:
                stack.append((cnode[0].left, cnode[0].left.val + cnode[1]))

            if cnode[0].right:
                stack.append((cnode[0].right, cnode[0].right.val + cnode[1]))

        return False
