class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        def checkFurther(s, words):
            n = len(s)

            for j in range(1, n):
                if s[0:j + 1] in words:
                    if j + 1 == n:
                        return True
                    if checkFurther(s[j + 1:], words):
                        return True
            return False


        words = set(wordDict)
        n = len(s)

        for j in range(1, n):
            currentWord = s[0:j + 1]
            if currentWord  in words:
                if checkFurther(s[j + 1:], words):
                    return True
        return False
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
sol = Solution()
print(sol.wordBreak(s,wordDict))