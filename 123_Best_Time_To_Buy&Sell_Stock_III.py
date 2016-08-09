class Solution(object):
    def maxProfit(self, prices):
        """
        Say you have an array for which the ith element is the price
        of a given stock on day i.

        Design an algorithm to find the maximum profit. You may complete
        at most two transactions.
        """
        if len(prices) <= 1:    return 0

        res = [[0 for dummy_j in range(len(prices))] for i in range(3)]
        """
        This is a dynamic programming problem.
        When there are nofTrans transactions allowed, for the first i days(up to i-1),
        the best transaction(s) is(are):
            res[nofTrans][i] = max(res[nofTrans][i-1], prices[i] - prices[j] + res[nofTrans-1][j] for j in range(i))
        The first case is that it's not a good choice to sell on the ith day.
        And in contrast, in the second case, we decide to sell on the ith day, thus we need to know what is the best
        time to divide the newly produced transaction and others.
        """
        for nofTrans in range(1, 3):
            tmax = res[nofTrans - 1][0] - prices[0]
            for i in range(1, len(prices)):
                res[nofTrans][i] = max(res[nofTrans][i - 1], tmax + prices[i] )
                tmax = max(tmax, res[nofTrans - 1][i] - prices[i])

        return res[-1][-1]
