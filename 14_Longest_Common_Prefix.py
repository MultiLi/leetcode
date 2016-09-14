# Find the longest common prefix of an array of strings.
# Other than making comparisons, avoiding the indices out of range

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return str("")

        if len(strs) == 1:
            return strs[0]

        res = []

        ind = 0

        char = ''

        while True:
            if ind < len(strs[0]):
                char = strs[0][ind]
            else:
                return ''.join(res)

            for s in range(1,len(strs)):
                if ind == len(strs[s]) or strs[s][ind] != char:
                    return ''.join(res)

            res.append(char)
            ind += 1

        return ''.join(res)
