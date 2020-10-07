'''
https://leetcode.com/problems/cheapest-flights-within-k-stops/
There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.
Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. 
If there is no such route, output -1.
Example 1:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200

Example 2:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
'''

# to find min cost, use dijkastra
# since there is not self cycle, dont maintain visited array, so that same node can be traversed again for shorter paths
from collections import defaultdict
from heapq import heappush, heappop
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int):
        
        graph = defaultdict(list)
        
        for s, d, price in flights:
            graph[s].append([d, price])
        
        heap = []
        heappush(heap, [0, src, K])
        
        while len(heap):

            summ, node, k = heap[0]
            heappop(heap)
            
            if node == dst and k >= -1:
                return summ
                
            elif k == -1:
                continue

            for neighbor, price in graph[node]:
                heappush(heap, [summ+price, neighbor, k-1])
            
        return -1