"""
Find Permutations of One string in another string
s1 = "abbc"
s2 = "cbabadcbbabbcbabaabccbabc"

Approach 1: Leetcode - Best Solution - Using Hashes

Approach 2: Brute force
Find all permutations of s1. Then find indices in s2 that have the permutations

"""


class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        slen = len(s)
        plen = len(p)
        if slen < plen:
            return []
        s = s.lower()
        p = p.lower()
        result = []
        shash = [0] * 26
        phash = [0] * 26
        for ch in p:
            phash[ord(ch) - ord('a')] += 1

        for i in range(plen - 1):
            shash[ord(s[i]) - ord('a')] += 1

        for i in range(plen - 1, slen):
            shash[ord(s[i]) - ord('a')] += 1
            if shash == phash:
                result.append(i - plen + 1)
            shash[ord(s[i- plen + 1]) - ord('a') ] -= 1

        return result


sol = Solution()
# s1 = "cbabadcbbabbcbabaabccbabc"
# s2 = "abcd"
s = "cbaebabacd"
p = "abc"

# s1 = "baa"
# s2 = "aa"
print(sol.findAnagrams(s,p))

