# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not (head and head.next):
            return head

        cnode = head

        while cnode.next:
            pcnode = cnode
            if pcnode.val == pcnode.next.val:
                while pcnode.next and pcnode.val == pcnode.next.val:
                    pcnode = pcnode.next
                cnode.next = pcnode.next
                cnode = pcnode
            else:
                cnode = cnode.next

        return head
