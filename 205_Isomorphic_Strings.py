class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        t1 = [0] * len(s)
        d = dict([])
        val = 1
        for ind in range(len(s)):
            if s[ind] not in d:
                d[s[ind]] = val
                val += 1
            t1[ind] = d[s[ind]]

        val = 1
        d = dict([])

        for ind in range(len(t)):
            if t[ind] not in d:
                d[t[ind]] = val
                val += 1
            if d[t[ind]] != t1[ind]:
                return False

        return True
