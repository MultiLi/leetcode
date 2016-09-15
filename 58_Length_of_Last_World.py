class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ':
                length -= 1
            else:
                break

        ind = 0
        count = 0

        while ind < length:
            if s[ind] == ' ':
                count = 0
            else:
                count += 1
            ind += 1
        return count
