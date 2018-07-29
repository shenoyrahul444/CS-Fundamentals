import string
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        wordset=set(wordList)
        if endWord not in wordset:
            return 0
        beginset={beginWord}
        endset={endWord}
        wordlen=len(beginWord)
        ladder=2
        while beginset:
            if len(beginset) > len(endset): # bidirectional BFS, start with the small set
                beginset, endset = endset, beginset
            next_beginset=set()
            for word in beginset:
                for i in range(wordlen):
                    word1,word2=word[:i],word[i+1:]
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        candidate=word1+c+word2
                        if candidate in endset:
                            return ladder
                        if candidate in wordset:
                            wordset.remove(candidate)
                            next_beginset.add(candidate)
            beginset = next_beginset
            ladder+=1
        return 0

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(Solution().ladderLength(beginWord,endWord,wordList))