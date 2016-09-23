class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = map(int, version1.split('.'))
        v2 = map(int, version2.split('.'))

        while True:
            if v1 and v1[-1] == 0:
                v1.pop()
            else:
                break

        while True:
            if v2 and v2[-1] == 0:
                v2.pop()
            else:
                break

        ind = 0
        length = min(len(v1), len(v2))
        while ind < length:
            if v1[ind] > v2[ind]:
                return 1

            elif v1[ind] < v2[ind]:
                return -1

            ind += 1

        if len(v1) > len(v2) :
            return 1

        elif len(v1) < len(v2):
            return -1

        else:
            return 0
