# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not (head and head.next):
            return head

        cnode = head.next
        pnode = head

        while cnode:
            tcnode = cnode.next
            cnode.next = pnode
            pnode = cnode
            cnode = tcnode

        head.next = None

        return pnode
