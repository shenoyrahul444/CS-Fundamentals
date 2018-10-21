class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board or not words:
            return []
        mem = {}
        for word in words:
            if word[0] not in mem:
                mem[word[0]] = [word]
            else:
                mem[word[0]].append(word)

        def dfs(i, j, word, ind):
            if ind == len(word):
                return True
            if i < 0 or j < 0 or i >= l or j >= b:
                return False
            if board[i][j] == word[ind]:
                temp = board[i][j]
                board[i][j] = "#"
                ans = dfs(i + 1, j, word, ind + 1) or dfs(i - 1, j, word, ind + 1) or dfs(i, j + 1, word,
                                                                                          ind + 1) or dfs(i, j - 1,
                                                                                                          word, ind + 1)
                board[i][j] = temp
                return ans
            return False

        completed = set()
        res = []
        l, b = len(board), len(board[0])
        for i in range(l):
            for j in range(b):
                if board[i][j] in mem:
                    s_words = mem[board[i][j]]
                    for word in s_words:
                        if word not in completed and dfs(i, j, word, 0):
                            res.append(word)
                            completed.add(word)
        return res

words = ["oath","pea","eat","rain"]
board =[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

sol = Solution()
print(sol.findWords(board,words))