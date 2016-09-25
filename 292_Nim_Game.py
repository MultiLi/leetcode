# The opponent can always make sure there're 4 stones removed in each turn.
# So if the total number of stones is divisible by 4, we can't win the game.
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return  (n % 4) != 0
