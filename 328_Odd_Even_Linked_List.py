# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Given a singly linked list, group all odd nodes together followed by the even
# nodes. Please note here we are talking about the node number and not the value
# in the nodes.
#
# You should try to do it in place. The program should run in O(1) space
# complexity and O(nodes) time complexity.
#
# Example:
# Given 1->2->3->4->5->NULL,
# return 1->3->5->2->4->NULL.

# Note:
# The relative order inside both the even and odd groups should remain as it was in the input.
# The first node is considered odd, the second node even and so on ...
class Solution(object):
    """
    The problem is I can't get a solution that is efficient enough.
    Just go throw the linked list, appending the values of all odd nodes to the
    result array , and merging all even nodes together. Finally, appending all
    these even nodes to the result array.
    """
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return []

        res = [head.val]
        pf = None

        if head.next :
            pf = head.next

            if head.next.next:
                pt = head.next
                pm = pt.next

                while True:
                    res.append(pm.val)
                    pt.next = pm.next
                    pt = pt.next
                    if pt and pt.next:
                        pm = pt.next
                    else: break

        while pf:
            res.append(pf.val)
            pf = pf.next

        return res
