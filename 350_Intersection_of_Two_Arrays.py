class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        hashm = dict()

        for num in nums1:

            if num not in hashm:
                hashm[num] = 1

            else:
                hashm[num] += 1
        ans = []
        for num in nums2:

            if num in hashm:
                ans.append(num)
                hashm[num] -= 1
                if not hashm[num]:
                    del hashm[num]

        return ans
