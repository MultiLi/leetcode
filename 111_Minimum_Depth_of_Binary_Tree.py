# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Implementing BFS

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        clayer = 0

        queue = [(root,1)]

        while queue:
            cnode = queue.pop(0)
            if cnode[1] > clayer:
                clayer = cnode[1]

            if not (cnode[0].left or cnode[0].right):
                break

            if cnode[0].left:
                queue.append((cnode[0].left,clayer + 1))

            if cnode[0].right:
                queue.append((cnode[0].right,clayer + 1))

        return clayer
