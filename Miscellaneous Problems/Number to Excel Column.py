class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n < 1:
            return ""
        res = ""
        while n > 0:
            res = chr((n%26 if n%26 != 0 else 26)+ 64) + res
            n -= 1
            n //= 26
        return res

sol = Solution()
print(sol.convertToTitle(701))
print(sol.convertToTitle(28))

