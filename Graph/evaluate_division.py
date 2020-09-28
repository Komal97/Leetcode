'''
https://leetcode.com/problems/evaluate-division/
You are given equations in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating-point number). Given some queries, return the answers. 
If the answer does not exist, return -1.0. The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.

Example 1:
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]

Example 2:
Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]

Example 3:
Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]
'''

# a/b means directed edge from a to b, save a to b and b to a in graph
# dfs - to find a/c -> a/b * b/c means path from a to c and keep on muliplying values
from collections import defaultdict
class Solution:
    
    def handleQuery(self, graph, num, den, visited):
        
        if num not in graph or den not in graph:
            return -1.0
        
        if num == den:
            return 1.0
        
        visited[num] = True                                             # mark node as visited
        res = -1
        for d, val in graph[num]:
            if not visited[d]:
                res = val * self.handleQuery(graph, d, den, visited)    # val = num/d and using recursion find d/den 
                if res >= 0:                                            # means we found a path because -ve denotes no path
                    break
                    
        visited[num] = False                                            # mark node unvisited so that it can be used in other query
        return res if res >= 0 else -1
    
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]):
        
        ans = []
        graph = defaultdict(list)
        visited = defaultdict(bool)
        for i, eq in enumerate(equations):
            num = eq[0]
            den = eq[1]
            graph[num].append([den, values[i]])                         # save num/den = value
            graph[den].append([num, 1.0/values[i]])                     # save den/num = 1/value

        for num, den in queries:
            res = self.handleQuery(graph, num, den, visited)
            ans.append(res)
        return ans