# Pure brute-force search

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        string = list(s)

        head = 0
        tail = len(s) - 1

        while head <= tail:
            if string[head] >= 'a' and string[head] <= 'z':
                pass
            elif string[head] >= 'A' and string[head] <= 'Z':
                string[head] = string[head].lower()
            elif string[head] >= '0' and string[head] <= '9':
                pass
            else:
                head += 1
                continue

            if string[tail] >= 'a' and string[tail] <= 'z':
                pass
            elif string[tail] >= 'A' and string[tail] <= 'Z':
                string[tail] = string[tail].lower()
            elif string[tail] >= '0' and string[tail] <= '9':
                pass
            else:
                tail -= 1
                continue

            if string[head] == string[tail]:
                head += 1
                tail -= 1

            else:
                return False

        return True
