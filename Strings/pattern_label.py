'''
https://leetcode.com/problems/partition-labels/
A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.
Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
'''
# method - 1 O(n^2)
# choose the smallest partition that includes the first letter. 
# last ptr points to end of 1 window, identified as last = max(j, last) of s[i]=s[j]
# at some i = last, at this condition we get one window
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        
        n = len(S)
        
        ans = []
        start = 0
        last = 0
        for i in range(n):
            for j in range(i, n):
                if S[i] == S[j]:
                    if j >= last:
                        last = j
            if i == last:
                ans.append(last-start+1)
                start = i+1
                last = i+1
        return ans

# method - 2 O(n) - same as prv logic
# keep last index of each character in map
# last ptr points to end of 1 window, identified as last = max(last, h[S[i]])
# at some i = last then append last-start+1, at this condition we get one window
class Solution:
    def partitionLabels(self, S: str):
        
        n = len(S)
        
        ans = []
        h = {c:i for i, c in enumerate(S)}
        start = 0
        last = 0
        for i in range(n):
            last = max(last, h[S[i]])
            if i == last:
                ans.append(last-start+1)
                start = i+1
                last = i+1
        return ans