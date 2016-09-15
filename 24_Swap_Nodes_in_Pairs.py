# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not ( head and head.next):
            return head

        prehead = ListNode(0)
        prehead.next = head

        node0 = prehead
        node1 = head
        node2 = head.next
        while node2:
            tnext = node2.next
            node2.next = node1
            node1.next = tnext
            node0.next = node2
            node0 = node1
            node1 = node0.next
            if not node1:
                break
            node2 = node1.next

        return prehead.next
