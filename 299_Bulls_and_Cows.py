class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        if not secret:
            return "0A0B"

        ind = 0
        hashm = dict()
        nofA = 0
        nofB = 0
        while ind < len(secret):
            if secret[ind] == guess[ind]:
                nofA += 1
                ind += 1
                continue

            if hashm and secret[ind] in hashm:
                if hashm[secret[ind]] < 0:
                    nofB += 1
                hashm[secret[ind]] += 1
            else:
                hashm[secret[ind]] = 1

            if hashm and guess[ind] in hashm:
                if hashm[guess[ind]] > 0:
                    nofB += 1
                hashm[guess[ind]] -= 1
            else:
                hashm[guess[ind]] = -1

            ind += 1

        return str(nofA)+ 'A' + str(nofB) + 'B'
                    
