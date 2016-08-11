# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# You are given two linked lists representing two non-negative numbers.
# The digits are stored in reverse order and each of their nodes contain a
# single digit. Add the two numbers and return it as a linked list.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        Kindda boring
        """
        if not (l1 or l2):
            return None
        if l1 and not l2:
            return l1
        if l2 and not l1:
            return l2
        root = l2
        f = 0
        while True:

            l2.val += l1.val + f
            f = 0

            if l2.val / 10:
                l2.val %= 10
                f = 1

            if not (l1.next or l2.next):
                if f:
                    l2.next = ListNode(1)
                break

            if l1.next and not l2.next:
                l2.next = l1.next
                while l2.next :
                    l2 = l2.next
                    l2.val += f
                    f = 0
                    if l2.val / 10:
                        l2.val %= 10
                        f = 1
                if f:
                    l2.next = ListNode(1)
                break

            if l2.next and not l1.next:
                while l2.next :
                    l2 = l2.next
                    l2.val += f
                    f = 0
                    if l2.val / 10:
                        l2.val %= 10
                        f = 1
                if f:
                    l2.next = ListNode(1)
                break

            l2 = l2.next
            l1 = l1.next

        return root
