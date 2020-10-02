'''
https://leetcode.com/problems/course-schedule/
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
'''

# detect cycle in directed graph
# maintain 3 states - 1 (need to visit), 2 (just visited and in path), 3 (all neighbors are traversed and no cycle) 
from collections import defaultdict
class Solution:

    ONE = 1                           # unvisited
    TWO = 2                           # visiting (neighbours are not traversed yet)
    THREE = 3                         # node and neighbors are visited
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]):
        
        graph = defaultdict(list)
        
        for s, e in prerequisites:
            graph[s].append(e)
            
        status = {i: Solution.ONE for i in range(numCourses)}
        
        def dfs(status, num):
            
            # mark visited
            status[num] = Solution.TWO                      
               
            for neighbor in graph[num]:
                # node not visited
                if status[neighbor] == Solution.ONE:      
                    dfs(status, neighbor)
                # node visited again in the same path means there is a cycle
                if status[neighbor] == Solution.TWO:       
                    return False
            
            # node and neighbors are visited
            status[num] = Solution.THREE                    
            return True
    
        for course in range(numCourses):
            if status[course] == Solution.ONE:
                if not dfs(status, course):
                    return False
                
        return True