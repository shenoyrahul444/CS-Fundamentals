class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits == [] or digits == None:
            return []

        for i in range(len(digits)):
            digits[i] = str(digits[i])

        s = "".join(digits)

        i = int(s) + 1
        # 1000
        res = []
        for digit in str(i):
            res.append(int(digit))

        return res

class Solution2:
    def plusOne(self,digits):

        if digits == None or digits == []:
            return []

        n = len(digits)
        num = 0
        for i in range(n):
            num += digits[n-1-i]*(10**i)

        num += 1
        res = []
        for digit in str(num):
            res.append(int(digit))

        return res

class Solution3:
    def plusOne(self,digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits == None or digits == []:
            return []
        n = len(digits)
        carry = 1
        for i in range(n):
            num = digits[n-1-i] + carry
            if num > 9:
                carry = 1
                digits[n-1-i] = 0
            else:
                digits[n-1-i] = num
                carry = 0
        if carry > 0:
            digits.insert(0,carry)
        return digits

sol = Solution2()
print(sol.plusOne([9,9,9]))