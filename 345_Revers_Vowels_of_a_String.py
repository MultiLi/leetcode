#Write a function that takes a string as input and reverse only the vowels of a
# string.
#
# Example 1:
# Given s = "hello", return "holle".
#
# Example 2:
# Given s = "leetcode", return "leotcede".
#
# Note:
# The vowels does not include the letter "y".

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return ''
        vowels = set(['a','e','i','o','u','A', "E", "I" , 'O', 'U'])
        stop = False
        ls = list(s)
        i = -1
        j = len(ls)

        while True:

            i += 1
            while i < len(ls) and ls[i] not in vowels:
                i += 1

            if i == len(ls) or j == i : break

            j -= 1
            while ls[j] not in vowels:
                j -= 1

            if j == i : break

            temp = ls[i]
            ls[i] = ls[j]
            ls[j] = temp

        return ''.join(ls)
