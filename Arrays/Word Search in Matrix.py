class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        h = len(board)
        w = len(board[0])
        result = []
        initials = {}
        for word in words:
            if word[0] in initials:
                initials[word[0]].append(word)
            else:
                initials[word[0]] = [word]
        for i in range(h):
            for j in range(w):
                if board[i][j] in initials:
                    for word in initials[board[i][j]]:
                        if self.checkWord(word, 1, i, j, board, h, w):
                            result.append(word)
        return result

    def checkWord(self, word, pos, i, j, board, h, w):

        letter = word[pos]
        neighbors = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        for row, col in neighbors:
            if 0 <= i + row < h and 0 <= j + col < w:
                if board[i + row][j + col] == letter :
                    if pos + 1 < len(word):
                        return self.checkWord(word, pos+1, i + row, j + col, board, h, w)
                    elif pos + 1 == len(word):
                        return True
        return False


sol = Solution()
words = ["oath","pea","eat","rain"]
board =[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

print(sol.findWords(board,words))