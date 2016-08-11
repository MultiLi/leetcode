# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Merge k sorted linked lists and return it as one sorted list. Analyze and
# describe its complexity.

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        In initialaiztion phase, iterate over the whole lists and push every
        (node, index in the lists) to a min-heap in which the key is the value
        of the node. During execution, in each iteration, the heap pops out a
        min-value node, after appending it on the result, append all its
        preceding nodes whose values are even smaller than the heap top. If the
        corresponding linked list runs out, fill its space in the lists with a
        None. Otherwise, replace it with the first bigger node.

        Complexity:

            Space: Except for the lists and all the linked lists themselves, the
            space complexity is just O(n) corresponding to the number of nodes,
            due to the result array. The size of the heap cannot be bigger than
            the lists, not to mention the result array.
            
            Time: In the worst case, for each node, we need to invoke each of
            push and pop operations. Since the heap is implemented in a binary
            tree manner, the worst case time complexity is overall O(nlogn).
        """
        if not lists: return None
        if len(lists) == 1:
            return lists[0]

        heap = []
        res = []
        flag = True

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, lists[i], i))

        while heap:

            hnode = heapq.heappop(heap)
            tnode = hnode[1]

            while tnode.next:

                res.append(tnode.val)
                tnode = tnode.next

                if heap and tnode.val >= heap[0][0]:
                    flag = False
                    break

            if not flag:
                lists[hnode[2]] = tnode
                heapq.heappush(heap, (tnode.val, tnode, hnode[2]))
                flag = True
            else:
                res.append(tnode.val)
                lists[hnode[2]] = None

        return res
