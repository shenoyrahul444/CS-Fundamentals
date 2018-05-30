import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        if n == 3:
            return 1
        arr = [True] * n
        arr[0] = arr[1] = False
        limit = int(math.sqrt(n))
        for i in range(2, limit + 1):
            if arr[i]:
                for j in range(i * i, n, i):
                    arr[j] = False
        c = 0
        for i in range(0,n):
            if arr[i]:
                c += 1
        return c


sol = Solution()
print(sol.countPrimes(13))
