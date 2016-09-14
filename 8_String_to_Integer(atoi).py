# Try to consider every possibilities, including spaces before the input,
# non-expected input character, and positive-negative symbl

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0

        i = 0
        end = -1
        while str[i] == ' ':
            end += 1
            i += 1

        multee = 1
        res = 0
        for i in range(len(str) - 1, end, -1):
            if str[i] > '9' or str[i] < '0':
                if i == end + 1:
                    if str[i] == '-':
                        res *= -1
                        break
                    elif str[i] == '+':
                        break
                    else:
                        return 0
                else:
                    res = 0
                    multee = 1
                    continue

            res += int(str[i]) * multee
            multee *= 10

        if res / (1 << 31)  > 0:
            res = (1 << 31) - 1
        elif res / (1 << 31) < -1:
            res = - ( 1<< 31 )

        return res
