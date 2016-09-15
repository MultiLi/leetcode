class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        if not nums:
            return 0

        ind = 0
        match = 0
        length = len(nums)

        while ind < len(nums):
            if nums[ind] == val:
                del nums[ind]
                match += 1
            else:
                ind += 1

        return length - match
