'''
https://leetcode.com/problems/course-schedule-ii/
There are a total of n courses you have to take labelled from 0 to n - 1.
Some courses may have prerequisites, for example, if prerequisites[i] = [ai, bi] this means you must take the course bi before the course ai.
Given the total number of courses numCourses and a list of the prerequisite pairs, return the ordering of courses you should take to finish all courses.
If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
'''

# use topological sort logic with directed graph cycle detection
from collections import defaultdict
class Solution:
    
    ONE = 1                           # unvisited
    TWO = 2                           # visiting (neighbours are not traversed yet)
    THREE = 3                         # node and neighbors are visited
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]):
        
        graph = defaultdict(list)
        for s, e in prerequisites:
            graph[s].append(e)
            
        status = {i: Solution.ONE for i in range(numCourses)}
        ans = []

        def dfs(status, num):
            
            status[num] = Solution.TWO
            for neighbor in graph[num]:
                if status[neighbor] == Solution.ONE:
                    dfs(status, neighbor)
                if status[neighbor] == Solution.TWO:
                    return False
                
            status[num] = Solution.THREE
            ans.append(num)
            return True

        for course in range(numCourses):
            if status[course] == Solution.ONE:
                if not dfs(status, course):
                    return []

        return ans
        