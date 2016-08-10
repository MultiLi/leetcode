# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# You are given a target value to search. If found in the array return its
# index, otherwise return -1.
#
# You may assume no duplicate exists in the array.

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        Try to traverse every possibility. Comments may makes this code even
        more unreadable.
        """
        if not nums: return -1

        if len(nums) == 1:
            return 0 if target == nums[0] else -1

        if nums[0] < nums[-1]:
            pivot = 0

        else:
            for i in range(1, len(nums)):
                if nums[i] < nums[i - 1]:
                    pivot = i
                    break

        if target < nums[pivot]:
            return -1
        elif target == nums[pivot]:
            return pivot
        elif target == nums[pivot - 1]:
            return pivot -1 if pivot else pivot + len(nums) - 1
        elif target > nums[pivot - 1]:
            return -1

        start, end = 0, len(nums) - 1

        res = -1

        while start <= end:

            ind = (end + start) / 2

            if target == nums[ind]:
                res = ind
                break

            elif target > nums[ind]:
                if pivot > ind:
                    start = ind + 1
                    end = pivot - 1
                elif target == nums[end]:
                    res = end
                    break
                elif target > nums[end]:
                    end = pivot - 1
                else:
                    start = ind + 1

            else:

                if pivot < ind:
                    start = pivot
                    end = ind -1
                elif target == nums[start]:
                    res = start
                    break
                elif target < nums[start]:
                    start = pivot
                else:
                    end = ind - 1

        return res
