class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        if len(nums) == 1:
            return 1

        ind = 0
        repeat = 0
        length = len(nums)
        while ind < len(nums) - 1:

            if nums[ind] == nums[ind + 1]:
                repeat += 1
                del nums[ind]
            else:
                ind += 1

        return length - repeat
