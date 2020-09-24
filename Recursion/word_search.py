'''
https://leetcode.com/problems/word-search/
Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
'''

class Solution:
    
    def exist(self, board: List[List[str]], word: str):
        
        def word_search(i, j, k):
            if k == s:
                return True
            
            if i < 0 or j < 0 or i >= n or j >= m or board[i][j] != word[k]:
                return False
            
            val = board[i][j]
            board[i][j] = ''
            for c in range(len(x)):
                flag = word_search(i + x[c], j + y[c], k + 1)
                if flag:
                    return True
            board[i][j] = val
            return False
        
        x = [1, -1, 0, 0]
        y = [0, 0, 1, -1]
        n, m, s = len(board), len(board[0]), len(word)            
        
        for i in range(n):
            for j in range(m):
                flag = word_search(i, j, 0)
                if flag:
                    return True
        return False
            
            
            
            
            
            
            
        