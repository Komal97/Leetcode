'''
https://leetcode.com/problems/word-search-ii/
Given a 2D board and a list of words from the dictionary, find all words in the board.
Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once in a word.
Example:
Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
'''

# store words in trie
# run dfs on board and check whether the current character is in trie, 
# if yes then move to children in trie and call in 4 directions in board and append character in output
# if we found terminal in Trie, means we found a string in board as well so append in ans
class Trie:
    class TrieNode:
        def __init__(self, data):
            self.data = data
            self.children = {}
            self.isTerminal = False

    def __init__(self):
        self.__root = self.TrieNode('')

    def getRoot(self):
        return self.__root

    def insert(self, word):

        temp = self.getRoot()
        for ch in word:
            if ch not in temp.children:
                child = self.TrieNode(ch)
                temp.children[ch] = child
                temp = child
            else:
                temp = temp.children[ch]
        temp.isTerminal = True
        
class Solution:
    
    x = [1, -1, 0, 0]
    y = [0, 0, 1, -1]
        
    def dfs(self, i, j, trienode, output, board, ans):
        
        if trienode.isTerminal:
            ans.add(output)
        
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] == '#' or board[i][j] not in trienode.children:
            return       
        

        val = board[i][j]
        board[i][j] = '#'
        for idx in range(len(self.x)):
            self.dfs(i + self.x[idx], j + self.y[idx], trienode.children[val], output + val, board, ans)

        board[i][j] = val
                
    def findWords(self, board: List[List[str]], words: List[str]):
    
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        ans = set()
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(i, j, trie.getRoot(), '', board, ans)
                
        return list(ans)