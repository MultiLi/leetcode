# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    Given a binary tree, return all root-to-leaf paths.

    Easy works, just binary depth-first search the tree.
    A little tricky to output arrows.
    
    """
    def findPath(self, root, path, res):
        path += str(root.val)
        if root.left and root.right:
            path += '->'
            self.findPath(root.left, path, res)
            npath = str(path)
            self.findPath(root.right, npath, res)
        elif not (root.left or root.right):
            res.append(path)
        else:
            tnode = root.left if root.left else root.right
            path += '->'
            self.findPath(tnode, path, res)

    def binaryTreePaths(self, root):
        if not root: return []
        path, res = str(), []
        self.findPath(root,path, res)
        return res
