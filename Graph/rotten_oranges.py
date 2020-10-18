'''
https://leetcode.com/problems/rotting-oranges/
In a given grid, each cell can have one of three values:
the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

Example 1:
Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
'''

# initially add all rotten orange in queue
# now run bfs, pop rotten add all surrounding fresh in queue
from collections import deque
class Solution:

    def orangesRotting(self, grid: List[List[int]]):
        
        n, m = len(grid), len(grid[0])
        rotten = deque()
        fresh = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    rotten.append([i, j, 0])
                elif grid[i][j] == 1:
                    fresh += 1

        min_time = 0
        while len(rotten):
            i, j, time = rotten.popleft()

            if grid[i][j] == 2:

                if i-1>=0 and grid[i-1][j] == 1:
                    grid[i-1][j] = 2
                    rotten.append([i-1, j, time+1])
                    fresh -= 1
                    
                if j-1>=0 and grid[i][j-1] == 1:
                    grid[i][j-1] = 2
                    rotten.append([i, j-1, time+1])
                    fresh -= 1
                    
                if i+1 < n and grid[i+1][j] == 1:
                    grid[i+1][j] = 2
                    rotten.append([i+1, j, time+1])
                    fresh -= 1
                    
                if j+1 < m and grid[i][j+1] == 1:
                    grid[i][j+1] = 2
                    rotten.append([i, j+1, time+1])
                    fresh -= 1

            if len(rotten) == 0:
                min_time = time
                
        return min_time if fresh == 0 else -1