'''
https://leetcode.com/problems/surrounded-regions/
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.A region is captured by flipping all 'O's into 'X's in that surrounded region.
Example:
X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:
X X X X
X X X X
X X X X
X O X X
Explanation:
Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. 
Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. 
Two cells are connected if they are adjacent cells connected horizontally or vertically.
'''

# call recursion from boundaries for 'O' and change them to special character
# We are left with 'X' and 'O' which are not on boundaries
# run 2 loops, change '.' to 'O' and 'O' to 'X'
class Solution:
    def solve(self, board: List[List[str]]):
        """
        Do not return anything, modify board in-place instead.
        """
        def flip(i, j):
            if i < 0 or j < 0 or i >= n or j >= m or board[i][j] == 'X' or board[i][j] == '.':
                return
            
            board[i][j] = '.'
            for k in range(len(x)):
                flip(i + x[k], j + y[k])
                
                
        if len(board) == 0:
            return
        if len(board[0]) == 0:
            return
        n, m = len(board), len(board[0])
        x = [1, -1, 0, 0]
        y = [0, 0, 1, -1]

        for i in range(m):
            if board[0][i] == 'O':
                flip(0, i)
            
            if board[n-1][i] == 'O':
                flip(n-1, i)
        
        for i in range(n):
            if board[i][0] == 'O':
                flip(i, 0)
            if board[i][m-1] == 'O':
                flip(i, m-1)
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == '.':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'