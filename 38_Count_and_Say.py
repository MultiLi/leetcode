class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        iter = 1
        new = '1'
        while iter < n:
            old = new
            new = ""
            ind = 0
            step = 1
            count = 1
            while ind < len(old):
                while ind + step < len(old) and old[ind] == old[ind + step]:
                    count += 1
                    step += 1
                new += str(count) + old[ind]
                ind += step
                step = 1
                count = 1

            iter += 1

        return new
