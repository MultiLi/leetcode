class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if not prices or len(prices) == 1:
            return 0

        maxpro = [0]* len(prices)
        passedLeast = prices[0]

        for sellby in range(1,len(prices)):
            maxpro[sellby] = max(maxpro[sellby - 1], prices[sellby] - passedLeast)
            passedLeast = min(passedLeast,  prices[sellby])

        return maxpro[-1]
