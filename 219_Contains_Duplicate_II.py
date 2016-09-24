class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums or len(nums) == 1:
            return False

        hashm = dict()

        ind = 0

        while ind < len(nums):

            if hashm and nums[ind] in hashm:
                if ind - hashm[nums[ind]] <= k:
                    return True
                else:
                    hashm[nums[ind]] = ind

            else:
                hashm[nums[ind]] = ind

            ind += 1

        return False
