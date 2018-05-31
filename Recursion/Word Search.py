class Solution1(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if board == None or word == None or board == [] or word == "":
            return False
        h, w = len(board), len(board[0])
        for i in range(h):
            for j in range(w):
                if board[i][j] == word[0]:
                    visited = [False] * (w * h)
                    if self.dfs(i, j, board, word, 0, visited):
                        return True
        return False

    def dfs(self, i, j, board, word, pos, visited):
        if pos == len(word) - 1:
            return True
        h, w = len(board), len(board[0])
        visited[(i * w) + j] = True
        neighbors = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        res = False
        for r, c in neighbors:
            new_row = i + r
            new_col = j + c
            if 0 <= new_row < h and 0 <= new_col < w and visited[new_row * w + new_col] == False:
                current_visited = visited[:]
                if pos + 1 < len(word) and board[new_row][new_col] == word[pos + 1]:
                    res = res or self.dfs(new_row, new_col, board, word, pos + 1, current_visited)
        return res


sol = Solution1()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

print(sol.exist(board,word))


class Solution2(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if board == []:
            return False

        def dfs(board, i, j, word):
            if len(word) == 0:
                return True
            if i < 0 or i >= m or j < 0 or j >= n or word[0] != board[i][j]:
                return False
            temp = board[i][j]
            board[i][j] = '#'
            res = dfs(board, i - 1, j, word[1:]) or dfs(board, i + 1, j, word[1:]) or dfs(board, i, j - 1,
                                                                                          word[1:]) or dfs(board, i,
                                                                                                           j + 1,
                                                                                                           word[1:])
            board[i][j] = temp
            return res

        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if dfs(board, i, j, word):
                    return True
        return False

