# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it is able to trap after raining.
#
# For example,
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

# Once on one side the maxheight is lower than the other side, it is able to
# contain some water, the volume of which is at most the maxheight of this
# side subtracted by the height of current location.

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        volume = 0
        head = 0
        tail = len(height) - 1
        lheight = 0
        rheight = 0
        while head < tail:
            lheight = max(lheight, height[head])
            rheight = max(rheight, height[tail])
            if lheight <= rheight:
                volume += lheight - height[head]
                head += 1
            else:
                volume += rheight - height[tail]
                tail -= 1

        return volume
