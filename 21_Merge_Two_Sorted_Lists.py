# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2

        elif not l2:
            return l1

        p1 = l1
        p2 = l2
        p1p = None
        p2p = None
        temptail = None

        res = l1 if l1.val< l2.val else l2

        while p1 and p2:
            p1h = p1
            p2h = p2
            if p1.val < p2.val:
                while p1 and p1.val < p2.val:
                    p1p = p1
                    p1 = p1.next
                p1p.next = p2
                p2p = p2
                if temptail:
                    temptail.next = p1h
                temptail = p2
                p2 = p2.next
            else:
                while p2 and p1.val >= p2.val:
                    p2p = p2
                    p2 = p2.next
                p2p.next = p1
                p1p = p1
                if temptail:
                    temptail.next = p2h
                temptail = p1
                p1 = p1.next

        if p1:
            temptail.next = p1
        else:
            temptail.next = p2

        return res
