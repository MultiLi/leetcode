# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Create a queue to do a bfs to the binary tree. By recording its current layer,
# judge if it is necessary to insert a new slot in the final array.

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        clayer = -1

        queue = [(root,0)]

        res = []

        while queue:
            cnode = queue.pop(0)
            if cnode[1] != clayer:
                clayer = cnode[1]
                res.append([])
            res[clayer].append(cnode[0].val)
            if cnode[0].left:
                queue.append((cnode[0].left, cnode[1] + 1))
            if cnode[0].right:
                queue.append((cnode[0].right, cnode[1] + 1))

        return res
