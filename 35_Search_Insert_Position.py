# Given a sorted array and a target value, return the index if the target is
# found. If not, return the index where it would be if it were inserted in order.
#
# You may assume no duplicates in the array.

# Here are few examples.
# [1,3,5,6], 5 → 2
# [1,3,5,6], 2 → 1
# [1,3,5,6], 7 → 4
# [1,3,5,6], 0 → 0

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

        Simple binary search
        """
        if not nums: return 0
        start, end = 0, len(nums)
        res = 0
        while start < end:
            l = start + (end - start - 1) / 2

            if target == nums[l]:
                return l

            if target > nums[l]:
                start = l + 1
            else:
                end = l

        return start
