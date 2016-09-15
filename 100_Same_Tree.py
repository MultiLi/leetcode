# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not (p or q):
            return True
        if (not p and q) or (not q and p):
            return False

        stackp = [p]
        stackq = [q]

        while stackp and stackq:
            cp = stackp.pop()
            cq = stackq.pop()
            if cp.val != cq.val:
                return False
            if cp.right and cq.right:
                stackp.append(cp.right)
                stackq.append(cq.right)
            elif not (cp.right or cq.right):
                pass
            else:
                return False
            if cp.left and cq.left:
                stackp.append(cp.left)
                stackq.append(cq.left)
            elif not (cp.left or cq.left):
                pass
            else:
                return False

        return True
