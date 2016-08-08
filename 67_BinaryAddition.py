class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        temp = int(a) + int(b)
        factor = 10
        while True:
            if temp % factor * 10 / factor >= 2:
                temp = temp + 8 * factor / 10

            if not temp / factor:
                break

            factor *= 10
        return str(temp)
