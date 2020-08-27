'''
https://leetcode.com/problems/is-graph-bipartite/
Given an undirected graph, return true if and only if it is bipartite.
Agraph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B.
The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  
Example 1:
Input: [[1,3], [0,2], [1,3], [0,2]]
Output: true
Explanation: 
The graph looks like this:
0----1
|    |
|    |
3----2
We can divide the vertices into two groups: {0, 2} and {1, 3}.
Example 2:
Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
Output: false
Explanation: 
The graph looks like this:
0----1
| \  |
|  \ |
3----2
We cannot find a way to divide the set of nodes into two independent subsets
'''

# put alternates vertices in a set - BFS
# if there is no cycle - means alternated edges can be added -  means bipartite
# if cycle - 1) if even, then alternate edges can be put -  means bipartite
#            2) if odd, then 1 node/edge is shared in 2 sets - not bipartite
# if cycle - same node appears 2 times in queue => if even then at same level and if odd then at different levels

from collections import deque
class Solution:
    
    def checkBipartite(self, graph, visited, src):
        
        q = deque()
        q.append([src, 0])
        
        while len(q) > 0:
            node, level = q.popleft()
            
            # check if node is not visited or if visited then not at same level means odd length cycle
            if visited[node] != -1 and visited[node] != level:      
                return False
            else:
                visited[node] = level
            
            for neighbour in graph[node]:
                if visited[neighbour] == -1:
                    q.append([neighbour, level+1])
        
        return True
    
    def isBipartite(self, graph: List[List[int]]):
        
        n = len(graph)
        
        # create visited array containing levels
        visited = [-1]*n
        
        for i in range(n):        
            # multiple components can be there, so if any component is not bipartite so ans is false                                  
            if visited[i] == -1:
                res = self.checkBipartite(graph, visited, i)
                if res == False:
                    return False
        return True