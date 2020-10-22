'''
https://leetcode.com/problems/clone-graph/
Given a reference of a node in a connected undirected graph. Return a deep copy (clone) of the graph.
Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

Test case format:
For simplicity sake, each node's value is the same as the node's index (1-indexed). For example, the first node with val = 1, the second node with val = 2, and so on. The graph is represented in the test case using an adjacency list.
Adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

Example 1:
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

Example 2:
Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

Example 4:
Input: adjList = [[2],[1]]
Output: [[2],[1]]
'''

'''
Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
'''

# method - 1
from collections import defaultdict, deque
class Solution:
    def cloneGraph(self, node: 'Node'):
        
        if node == None:
            return None
        
        visited = defaultdict(bool)
        copyvisited = defaultdict()
        queue = deque()
        
        src = Node(node.val)
        queue.append([node, src])
        copyvisited[node.val] = src
        
        while len(queue) > 0:
            
            original, copy = queue.popleft()
            visited[original] = True
            
            for nbr in original.neighbors:
                # if node is not visited
                if not visited[nbr]:                                
                    # if node is already created by some other node then refer that node else create
                    if nbr.val not in copyvisited:                  
                        child = Node(nbr.val)
                        copyvisited[nbr.val] = child
                    else:
                        child = copyvisited[nbr.val]

                    copy.neighbors.append(child)
                    child.neighbors.append(copy)
                
                    queue.append([nbr, child])
        
        return src
    
# method - 2
from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node'):
        
        if node == None:
            return None
        
        # keep mapping of node: clone
        clone = {}
        queue = deque()
        cloneroot = Node(node.val)
        
        clone = {node: cloneroot}
        queue.append(node)
        
        while len(queue) > 0:
            
            n = queue.popleft()
            
            # process all neighbors of node 
            for nbr in n.neighbors:
                # if node is not created then create, add in map and queue
                if nbr not in clone:
                    child = Node(nbr.val)
                    clone[nbr] = child
                    queue.append(nbr)
                # if already created then only refer and no need to append in queue as it is seen already and processed
                # but needed to be connect by some other node
                else:
                    child = clone[nbr]
                # always append the neighbors
                clone[n].neighbors.append(child)
        
        return cloneroot
        
        