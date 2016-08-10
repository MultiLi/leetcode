# Given a sorted positive integer array nums and an integer n, add/patch
# elements to the array such that any number in range [1, n] inclusive can be
# formed by the sum of some elements in the array. Return the minimum number of
# patches required.
#
# Example 1:
# nums = [1, 3], n = 6
# Return 1.
#
# Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
# Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3],
# [2,3], [1,2,3].
# Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
# So we only need 1 patch.

class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        A real genius invents this algorithm.
        It is a greedy algorithm. By defining the upper-bound of the values
        reachable by discovered numbers, it shows that if there is a "hole",
        then we should make it up by the upper-bound itself.
        
        """
        m, i, res = 1, 0 , 0
        while m <= n:
            if i < len(nums) and nums[i] <= m:
                m += nums[i]
                i += 1
            else:
                m += m
                res += 1

        return res
