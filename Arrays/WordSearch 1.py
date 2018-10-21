class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if board == None or word == None or board == [] or word == "":
            return False

        def dfs(i, j, ind):
            if ind == len(word):
                return True
            if i < 0 or i >= l or j < 0 or j >= b:
                return False
            if board[i][j] == word[ind]:
                temp = board[i][j]
                board[i][j] = "#"
                ans = dfs(i + 1, j, ind + 1) or dfs(i - 1, j, ind + 1) or dfs(i, j + 1, ind + 1) or dfs(i, j - 1,
                                                                                                        ind + 1)
                board[i][j] = temp
                return ans
            return False

        l, b = len(board), len(board[0])
        for i in range(l):
            for j in range(b):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False

board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

testcases = [["ABCCED", True],["SEE", True],["ABCB", False]]
sol = Solution()
for ip,op in testcases:
    print(sol.exist(board,ip) == op)
