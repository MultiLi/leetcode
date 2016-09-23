# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None
        while head.val == val:
            if head.next:
                head = head.next
            else:
                return None
        if head.next:
            cnode = head.next
        else:
            return head

        pnode = head

        while True:
            if cnode.val == val:
                pnode.next = cnode.next
                cnode = pnode.next
                if not cnode:
                    return head

            elif cnode.next:
                pnode = cnode
                cnode = cnode.next

            else:
                return head
