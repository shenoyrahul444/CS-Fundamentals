"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.
Example 1:
Input:s1 = "ab" s2 = "eidbaooo"
Output:True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False
Note:
The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].

"""
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        def permutations(string):
            if len(string) == 1:
                return [string]
            res = []
            for i in range(len(string)):
                for permu in permutations(string[:i] + string[i + 1:]):
                    res.append(string[i] + permu)
            return res

        if not s1 or not s2:
            return False

        if len(s1) == 1 and len(s2) >= len(s1):
            return s2.find(s1) > -1

        for i in range(len(s1)):
            res = []
            for perm in permutations(s1[:i] + s1[i + 1:]):
                if s2.find(s1[i]+perm) > -1:
                    return True
        return False

sol = Solution()
s1 = "hello"
s2 = "ooolleoooleh"
print(sol.checkInclusion(s1,s2))