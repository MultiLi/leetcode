class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k < 0 or k >= len(nums) - 1:
            return

        ind = k + 1

        while ind < len(nums):
            temp = nums[ind]
            iind = ind
            while iind >= ind - k:
                nums[iind] = nums[iind - 1]
                iind -= 1

            nums[iind] = temp
            ind += 1
        return
