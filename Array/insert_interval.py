'''
https://leetcode.com/problems/insert-interval/
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.
Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Example 3:
Input: intervals = [], newInterval = [5,7]
Output: [[5,7]]

Example 4:
Input: intervals = [[1,5]], newInterval = [2,3]
Output: [[1,5]]

Example 5:
Input: intervals = [[1,5]], newInterval = [2,7]
Output: [[1,7]]
'''

class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]):
        
        
        ans = []
        for i in range(len(intervals)):
            
            # if interval is completely independent
            if intervals[i][1] < new_interval[0]:
                ans.append(intervals[i])
                
            # if new interval is completely independent
            elif new_interval[1] < intervals[i][0]:
                ans.append(new_interval)
                new_interval = intervals[i]
                
            # create a new merged interval
            else:
                new_interval[0] = min(new_interval[0], intervals[i][0])
                new_interval[1] = max(new_interval[1], intervals[i][1])
                
        ans.append(new_interval)
    
        return ans
