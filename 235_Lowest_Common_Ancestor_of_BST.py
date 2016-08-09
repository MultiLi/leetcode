# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two
# given nodes in the BST.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor
# is defined between two nodes v and w as the lowest node in T that has both v
# and w as descendants (where we allow a node to be a descendant of itself).”
#
#        _______6______
#       /              \
#    ___2__          ___8__
#   /      \        /      \
#  0      _4       7       9
#        /  \
#       3   5
# For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another
# example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of
# itself according to the LCA definition.

class Solution(object):
    """
    If p and q are in different subtrees of current node, then it is the answer.
    Else, iteratively go down to the subtree in which they locate. 
    """
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val > q.val:
            small = q.val
            big = p.val
        else:
            small = p.val
            big = q.val
        tnode = root
        res = 0
        while tnode:
            if small > tnode.val:
                tnode = tnode.right
            elif big < tnode.val:
                tnode = tnode.left
            else:
                res = tnode.val
                break
        return res
