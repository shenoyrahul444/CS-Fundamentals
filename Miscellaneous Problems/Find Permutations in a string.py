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

        dic1, dic2, m, n, result = [0] * 26, [0] * 26, len(s), len(p), []
        for letter in p:
            dic1[ord(letter) - 97] += 1
        for i in range(min(m, n)):
            dic2[ord(s[i]) - 97] += 1
        if dic1 == dic2:
            result.append(0)
        for i in range(n, m):
            dic2[ord(s[i]) - 97] += 1
            dic2[ord(s[i - n]) - 97] -= 1
            if dic1 == dic2:
                result.append(i - n + 1)
        return result

sol = Solution()
# s1 = "abcd"
# s2 = "cbabadcbbabbcbabaabccbabc"

# s1 = "baa"
# s2 = "aa"
# print(sol.findAnagrams(s2,s1))

class Solution1:
    def findPerm(self,s1,s2):
        perms = self.getPerm(s1)
        res = []
        for perm in perms:
            ind  = s2.find(perm)
            if ind != -1:
                res.append(ind)
        return res



    def getPerm(self,s1):
        if s1 == "":
            return [""]

        res = []
        for i in range(len(s1)):
            letter = s1[i]
            for perm in self.getPerm(s1[:i]+ s1[i+1:]):
                res.append(letter + perm)
        return res

# sol = Solution()
# s1 = "abcd"
# s2 = "cbabadcbbabbcbabaabccbabc"

# print(sol.findPerm(s1,s2))


class Solution2:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        def getAnagrams(str):
            if str == "":
                return [""]
            res = []
            for i in range(len(str)):
                current_letter = str[i]
                for ang in getAnagrams(str[:i] + str[i + 1:]):
                    res.append(current_letter + ang)
            return res

        anagrams = getAnagrams(p)
        unique_anagrams = set(anagrams)
        positions = []
        for ang in unique_anagrams:
            if s.find(ang) == -1:
                continue
            first_occurance = s.find(ang)
            positions.append(first_occurance)
            start = first_occurance +1
            while s.find(ang, start) != -1:
                next_occurance = s.find(ang, start)
                positions.append(next_occurance)
                start = next_occurance+1
        return positions

sol = Solution2()
# s1 = "cbabadcbbabbcbabaabccbabc"
# s2 = "abcd"

# s1 = "baa"
# s2 = "aa"
# print(sol.findAnagrams(s1,s2))


class Solution4:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        slen = len(s)
        plen = len(p)
        result = []
        i = 0
        while i < slen:
            element = s[i]
            ind = p.find(s[i])
            if ind != -1:
                retVal = self.checkMatch(i+1, 1, s, p[:ind]+p[ind + 1:], plen)
                if retVal == -1:
                    result.append(i)
                    i += 1
                else:
                    i = retVal
            else:
                i += 1
        return result

    def checkMatch(self, pos, ctr, s, p, plen):
        if ctr == plen:
            return -1
        if pos< len(s):
            element = s[pos]
            ind = p.find(s[pos])
            if ind == -1:
                return pos
            else:
                return self.checkMatch(pos+1, ctr + 1, s, p[:ind] + p[ind + 1:], plen)
        else:
            return pos + plen

sol = Solution4()
# s = "cbabadcbbabbcbabaabccbabc"
# p = "abcd"

# s = "cbaebabacd"
# p  = "abc"
s = "abab"
p = "ab"
print(sol.findAnagrams(s,p))

class Solution5:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        n, m = len(s), len(p)
        if n < m: return res
        phash, shash = [0]* 26, [0] * 26
        for x in p:
            phash[ord(x) - ord('a')] += 1
        for x in s[:m - 1]:
            shash[ord(x)-ord('a')] += 1
        for i in range(m - 1, n):
            shash[ord(s[i])-ord('a')] += 1
            if i - m >= 0:
                shash[ord(s[i - m])-ord('a')] -= 1
            if shash == phash:
                res.append(i - m + 1)
        return res

# sol = Solution5()
# # s = "cbabadcbbabbcbabaabccbabc"
# # p = "abcd"
#
# s = "cbaebabacd"
# p  = "abc"
# print(sol.findAnagrams(s,p))