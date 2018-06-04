"""
Given an input string , reverse the string word by word.

Example:

Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
Note:

A word is defined as a sequence of non-space characters.
The input string does not contain leading or trailing spaces.
The words are always separated by a single space.
Follow up: Could you do it in-place without allocating extra space?
"""

""" SOLUTION 1 """
class Solution1(object):
    def reverseWords(self, string):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        def reverse(s,start,end):
            while start<end:
                s[start],s[end] = s[end],s[start]
                start += 1
                end -= 1
            return s

        n = len(string)
        i = 0

        for j in range(n):
            if string[j] == " ":
                reverse(string,i,j-1)
                i= j+1
        reverse(string, i , n - 1)
        # reverse(string, 0 , n - 1)
        return string
sol = Solution1()
stri = "Rahul is Great"
print(stri)
print("\n** After Reversal **\n")
sol.reverseWords(stri)
print(stri)



""" SOLUTION 2 ----------------> IF DONE SEPARATELY. NOT INPLACE """
# class Solution2(object):
#     def reverseWords(self, str):
#         """
#         :type str: List[str]
#         :rtype: void Do not return anything, modify str in-place instead.
#         """
#         if str == None or str == "":
#             return -1
#
#         words = "".join(str).split(" ")
#         n = len(words)
#
#         i=0
#         j=n-1
#         while  i<j:
#             words[i], words[j] = words[j], words[i]
#             i+=1
#             j-=1
#
#         # mid = n // 2 if n % 2 == 0 else (n % 2 + 1)
#         #
#         # for i in range(mid):
#         #     words[i], words[n - 1 - i] = words[n - 1 - i], words[i]
#         return " ".join(words)
#
# sol = Solution2()

# print(sol.reverseWords("Rahul Is Great"))
# Result ---> "Great Is Rahul"