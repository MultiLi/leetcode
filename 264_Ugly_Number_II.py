# Find the nth ugly number which is divisible of only 2,3 and 5.
# The 1st ugly number is 1

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int

        In each iteration, append a new ugly number which is the minimum in
        2, 3 or 5 times previous new ugly numbers.
        Get this solution from dicussion section
        """
        if n <= 3:
            return n

        ug = [1 for i in range(n + 1)]
        ct,i2,i3,i5=1,1,1,1
        while ct<n:
            while 2*ug[i2]<=ug[ct]:
                i2+=1
            while 3*ug[i3]<=ug[ct]:
                i3+=1
            while 5*ug[i5]<=ug[ct]:
                i5+=1
            ct+=1
            ug[ct] = min(2*ug[i2],3*ug[i3],5*ug[i5])

        return ug[n]
