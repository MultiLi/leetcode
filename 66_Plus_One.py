class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        if not digits:
            return [1]

        cp = False

        for i in range( len(digits) - 1, -1, -1):
            if digits[i] + 1 == 10:
                digits[i] = 0
                cp = True
            else:
                digits[i] += 1

            if cp:
                cp = False
                if i == 0:
                    digits.insert(0, 1)
            else:
                break

        return digits
