# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Given a linked list, return the node where the cycle begins. If there is no
# cycle, return null.
#
# Note: Do not modify the linked list.

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        Use a pair of fast-slow pointers. Initialize them as the head pointer of
        the linked list, in each iteration, the faster one takes 2 steps while
        the slower 1. If there is a loop, they will meet again. If at that time
        k iterations has passed, k is exactly the length of the loop, and also
        the distance from the head to the current node. So, when 2 pointers
        starts from the head and the current node will meeat at where the cycle
        begins.
        """

        if not head:
            return None
        p = head
        q = head
        while True:
            if not (p.next and q and q.next):
                return None
            p = p.next
            q = q.next.next
            if p == q:
                break
        while p != head:
            p = p.next
            head = head.next

        return head
