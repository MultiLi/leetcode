class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        nums = str(num)

        while len(nums) > 1:
            temp = sum(map(int,nums))
            nums = str(temp)

        return int(nums)
