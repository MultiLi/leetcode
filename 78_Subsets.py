class Solution(object):
    """
    Given a set of distinct integers, nums, return all possible subsets.

    Note: The solution set must not contain duplicate subsets.

    For example,
        If nums = [1,2,3], a solution is:

        [
        [3],
        [1],
        [2],
        [1,2,3],
        [1,3],
        [2,3],
        [1,2],
        []
        ]
    """

    def recSub(self, nums, length, res):
        """
        Do a set of binary recursive operations, to make each elements appear or
        disappear in the produced subset
        """
        if length == 0 or len(nums) == 0:
            return res
            
        self.recSub(nums, length - 1, res)
        new = list(nums)
        del new[length - 1]
        res.append(new)
        self.recSub(new, length - 1, res)
        return res

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [nums]
        self.recSub(nums, len(nums), res)
        return res
