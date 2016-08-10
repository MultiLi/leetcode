class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Circuler Version of Prob. 198.
        Decompose the original circular problem to 2 subproblems, odd and even,
        and deal with them separately by dynamic programming piradigm.
        """
        if not nums:
            return 0

        if len(nums) <= 2:
            return max(nums)

        res1 = [0 for i in range(len(nums) - 1)]
        res2 = [0 for i in range(len(nums) - 1)]

        res1[0] = nums[0]
        res2[0] = nums[1]
        res1[1] = max(nums[0], nums[1])
        res2[1] = max(nums[1],nums[2])

        for i in range(2, len(nums) - 1):
            res1[i] = max(res1[i-1], res1[i-2] + nums[i])
            res2[i] = max(res2[i-1], res2[i-2] + nums[i + 1])

        return max(res1[-1],res2[-1])
