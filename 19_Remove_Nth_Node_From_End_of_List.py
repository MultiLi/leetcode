# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return None

        cnode = head
        lnode = head

        i = 0
        while i < n:
            cnode = cnode.next
            i += 1

        j = 0

        if not cnode:
            head = head.next

        else:
            while cnode.next:
                cnode = cnode.next
                lnode = lnode.next


        lnode.next = lnode.next.next

        return head
