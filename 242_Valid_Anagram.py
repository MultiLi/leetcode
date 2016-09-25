class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        hashm = dict()
        for char in s:
            if hashm and char in hashm:
                hashm[char] += 1

            else:
                hashm[char] = 1

        print hashm

        for char in t:
            if char in hashm:
                if hashm[char] != 1:
                    hashm[char] -= 1
                else:
                    del hashm[char]

            else:
                return False

        if not hashm:
            return True
        else:
            return False
