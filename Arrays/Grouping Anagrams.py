class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if strs == None or strs == []:
            return strs
        anagrams = {}
        for anagram in strs:
            sorted_anagram = "".join(sorted(anagram))
            if sorted_anagram in anagrams:
                anagrams[sorted_anagram].append(anagram)
            else:
                anagrams[sorted_anagram] = [anagram]
        return anagrams.values()

sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))