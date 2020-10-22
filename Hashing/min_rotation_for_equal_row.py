'''
https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the ith domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)
We may rotate the ith domino, so that A[i] and B[i] swap values.
Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.
If it cannot be done, return -1.

Example 1:
Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.

Example 2:
Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
Output: -1
Explanation: 
In this case, it is not possible to rotate the dominoes to make one row of values equal.
'''

# to find swapping element
# keep map for freqA, freqB and freqCommon
# then run loop 1 to 6, if freqA[i] + freqB[i] - freqCommon[i] >= len(array) means this element needs swapping
# keep ans = min(ans, n-freqA[i], n-freqB[i]) to find minimum swaps
from collections import defaultdict
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]):
        
        n = len(A)
        mapA = defaultdict(int)
        mapB = defaultdict(int)
        mapCommon = defaultdict(int)
        
        for i in range(n):
            mapA[A[i]] += 1
            mapB[B[i]] += 1
            if A[i] == B[i]:
                mapCommon[A[i]] += 1
    
        ans = float('inf')
        for i in range(1, 7):
            if mapA[i] + mapB[i] - mapCommon[i] >= n:
                ans = min(ans, n-mapA[i], n-mapB[i])
                
        return ans if ans != float('inf') else -1

        
        