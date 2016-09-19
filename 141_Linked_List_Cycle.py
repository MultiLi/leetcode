# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        singleStep = head
        doubleStep = head

        while True:
            if singleStep.next:
                singleStep = singleStep.next

            else:
                return False

            if doubleStep.next:
                doubleStep = doubleStep.next

            else:
                return False

            if doubleStep.next:
                doubleStep = doubleStep.next

            else:
                return False

            if singleStep == doubleStep:
                return True
