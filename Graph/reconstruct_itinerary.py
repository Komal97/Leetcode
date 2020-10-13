'''
https://leetcode.com/problems/reconstruct-itinerary/
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. 
All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.
Note:
If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. 
One must use all the tickets once and only once.
Example 1:
Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]

Example 2:
Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is larger in lexical order.

Example 3:
Input: [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
Output: ["JFK","NRT","JFK","KUL"]
'''

# use heap to make array sorted so that traversal become lexiographically
# use tolopological sort method for traversal because we have to find node which become last in traversal and trace our path back
from heapq import heappush, heappop, heapify
class Solution:
    def findItinerary(self, tickets: List[List[str]]):
        
        graph = collections.defaultdict(list)
        
        for fro, to in tickets:
            heappush(graph[fro], to)
        
        ans = []
        
        def dfs(node):
           
            while len(graph[node]) > 0:
                val = graph[node][0]
                heappop(graph[node])
                dfs(val)
            
            ans.append(node)
                
        dfs('JFK')
        return ans[::-1]
    
    