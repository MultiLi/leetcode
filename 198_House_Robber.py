# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed, the only constraint stopping
# you from robbing each of them is that adjacent houses have security system
# connected and it will automatically contact the police if two adjacent houses
# were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of
# each house, determine the maximum amount of money you can rob tonight without
# alerting the police.

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Such a standard dynamic programming problem.
        The first time I get the correct solution without making any mistakes.
        """
        if not nums:
            return 0

        if len(nums) <= 2:
            return max(nums)

        res = [0 for i in range(len(nums))]

        res[0] = nums[0]
        res[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            res[i] = max(res[i-1], res[i-2] + nums[i])

        return res[-1]
