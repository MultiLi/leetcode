# Given a pattern and a string str, find if str follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a
# letter in pattern and a non-empty word in str.
#
# Examples:
# pattern = "abba", str = "dog cat cat dog" should return true.
# pattern = "abba", str = "dog cat cat fish" should return false.
# pattern = "aaaa", str = "dog cat cat dog" should return false.
# pattern = "abba", str = "dog dog dog dog" should return false.
# Notes:
# You may assume pattern contains only lowercase letters, and str contains
# lowercase letters separated by a single space.

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        A naive solution with a hash table
        """
        if not (pattern and str): return False

        tstr = str.split(' ')
        if len(pattern) != len(tstr): return False
        if len(set(pattern)) != len(set(tstr)): return False

        vocab = dict()
        for i in range(len(tstr)):
            if vocab and vocab.has_key(tstr[i]):
                if pattern[i] != vocab[tstr[i]]:
                    return False
            else:
                vocab[tstr[i]] = pattern[i]

        return True
