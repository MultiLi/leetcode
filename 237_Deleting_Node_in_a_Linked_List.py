# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        Really easy
        """
        tnode = node
        while tnode.next:
            tnode.val = tnode.next.val
            if not tnode.next.next:
                break
            tnode = tnode.next

        tnode.next = None

        return
