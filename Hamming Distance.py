class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        bin_x, bin_y = bin(x)[2:], bin(y)[2:]

        if len(bin_y) > len(bin_x):
            return self.hammingDistance(y, x)
        diff = len(bin_x) - len(bin_y)
        for i in range(diff):
            bin_y = "0" + bin_y

        count = 0
        for i in range(len(bin_x)):
            if bin_x[i] != bin_y[i]:
                count += 1

        return count
class Solution2:
    def hammingDistance(self,x,y):
        pass

sol = Solution()
# sol.hammingDistance(1,4)
# a = 1
# for b in range(2,6):
#     print(bin(a))
#     print(bin(b))
#     print(bin(a^b))
#     print(a^b)
#     print("\n")

print(1-3.2)
print(5-3.2)