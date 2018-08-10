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

# Approach 1: Create all permutations of s1 in O(n!) and then compare each permutation to the s2 as the window slides O(n)
"So O(n*n!).......It cant get more inefficient..Brute force approach, but a good start for the thought process"

# Approach 2: Using Hashing -> Hash s1, and compare it to the sliding hashes of size len(s1) on s2

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # Edge cases
        if s1 == None or s2 == None:
            return False
        n1 = len(s1)
        n2 = len(s2)
        if n2 < n1:
            return False

        a1 = [0] * 26
        # Hashing s1 in a1 -> Our reference window
        for c in s1:
            if c.isalpha():
                a1[ord(c) - ord('a')] += 1

        a2 = [0] * 26
        for i in range(n1):
            a2[ord(s2[i]) - ord('a')] += 1

        if a1 == a2:
            return True

        for i in range(n1, n2):
            a2[ord(s2[i]) - ord('a')] += 1
            a2[ord(s2[i - n1]) - ord('a')] -= 1
            if a1 == a2:
                return True
        return False

sol = Solution()
s1= "ab"
s2 = "eidboaoo"
print(sol.checkInclusion(s1,s2))

s3 = "ab"
s4 = "eidbaooo"
print(sol.checkInclusion(s3,s4))