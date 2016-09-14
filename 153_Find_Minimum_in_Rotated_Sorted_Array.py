class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        i = 1
        while i < len(nums):
            if nums[i] < nums[i - 1]:
                res = nums[i]
                break
            i += 1
        return res
