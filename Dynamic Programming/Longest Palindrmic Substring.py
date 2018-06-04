"""
Given a string, find the largest palindromic Subsequence
Example:
 Given a string "ABCBAABCBT"
 Largest Palindomic subsequence for the string would be: "BCBAABCB"
"""

"""Solutions
1> First way is find all the subsequences in the string, Both O(n2) for time and space complexiety . Then for each subsequence check if it is a palindrome, [O(s1)+ O(s2) + O(s3)......(sn)].
    This is a very computationally expensive task with a lot of spaace requirement.

2> We can use dynamic programming to solve this problem in O(n2) Time and Space complexiety.

3> 
"""
""" O(n) time - 59 millisecond submission """

class BestSolution:
    def longestPalindrome(self,s):
        if not s:
            return s

        start = 0
        end = 0
        n = len(s)
        for i in range(n):
            len1 = self.checkAroundCenter(s,i,i)
            len2 = self.checkAroundCenter(s,i,i+1)
            max_len = max(len1,len2)
            if max_len > end - start:
                start = i - (max_len - 1)//2
                end = i + (max_len)//2

        return s[start:end+1]

    def checkAroundCenter(self,s, left, right):
        L = left
        R = right

        while L >= 0 and R < len(s) and s[L] == s[R]:
            L -= 1
            R += 1

        return R - L - 1

sol = BestSolution()
# s = "BABABDA"
s = "CBBD"
print(sol.longestPalindrome(s))

class Solution1(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)<2 or s==s[::-1]:
            return s
        n=len(s)
        start,maxlen=0,1
        for i in range(n):
            odd =s[i-maxlen-1:i+1] #len(odd)=maxlen+2
            even=s[i-maxlen:i+1]    #len(even)=maxlen+1
            if i-maxlen-1>=0 and odd==odd[::-1]:
                start=i-maxlen-1
                maxlen+=2
                continue
            if i-maxlen>=0 and even==even[::-1]:
                start=i-maxlen
                maxlen+=1
        return s[start:start+maxlen]
# sol = Solution1()
# print(sol.longestPalindrome("ACCABAT"))


""" 88 Millisecond Solution """
class Solution2(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)==0:
        	return 0
        maxLen=1
        start=0
        for i in range(len(s)):
        	if i-maxLen >=1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]:
        		start=i-maxLen-1
        		maxLen+=2
        		continue

        	if i-maxLen >=0 and s[i-maxLen:i+1]==s[i-maxLen:i+1][::-1]:
        		start=i-maxLen
        		maxLen+=1
        return s[start:start+maxLen]

sol = Solution2()
# print(sol.longestPalindrome("ACCAT"))
class Solution3:
    def getLongestPalindromicString(self, s):
        # print(s)
        if s == None:
            return -1
        n = len(s)
        if n == 1:
            return s

        if n == 2:
            if s[0] == s[1]:
                return s
            else:
                return -1

        table = [[0 for i in range(n)] for j in range(n)]

        maxlength = 1
        i = 0
        while i < n:
            table[i][i] = True
            i += 1
        # print(table)

        """ For finding 2 letter words that are same"""
        start = 0
        i = 0
        while i < n - 2:
            if s[i] == s[i + 1]:
                table[i][i + 1] = True
                maxlength = 2
                start = i
            i += 1

        """ For sequences greater than length 3"""
        k = 3
        while k <= n:
            i = 0
            while i < n - k + 1:
                j = i + k - 1

                if table[i + 1][j - 1] and s[i] == s[j]:
                    table[i][j] = True

                    if k > maxlength:
                        maxlength = k
                        start = i
                i += 1
            k += 1



        # print("Maxlength", maxlength)
        # print("Start", start)
        # end_index = start + maxlength - 1
        # print(start + maxlength - 1)
        # print("Largest Palindromic Subsequence : " + s[start:start + maxlength])
        # return(s[start:start + maxlength])
        return maxlength

sol = Solution3()
# print(sol.getLongestPalindromicString("ACCBAT"))

