# O(n) build a sum array, in which the ith element is the sum of 0 to i.
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums

        ind = 1

        while ind < len(nums):

            self.nums[ind] += self.nums[ind - 1]
            ind += 1

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """

        if not i:
            return self.nums[j]

        else:
            return self.nums[j] - self.nums[i - 1]



# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)
