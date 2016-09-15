class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if not needle:
            return 0

        if not haystack or len(haystack) < len(needle):
            return -1

        ind = 0
        res = 0
        while ind + len(needle) <= len(haystack):
            indi = 0
            indt = ind
            res = ind
            while indt < len(haystack) :
                if haystack[indt] == needle[indi]:
                    indt += 1
                    indi += 1
                    if indi == len(needle):
                        return res
                else:
                    break
            ind += 1

        return -1
