class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ind = 0
        candidate = 0
        nTimes = 0

        while ind< len(nums):

            if nTimes == 0:
                nTimes = 1
                candidate = nums[ind]

            else:
                if candidate == nums[ind]:
                    nTimes += 1

                else:
                    nTimes -= 1

            ind += 1

        return candidate
