'''
https://leetcode.com/problems/reach-a-number/
You are standing at position 0 on an infinite number line. There is a goal at position target.
On each move, you can either go left or right. During the n-th move (starting from 1), you take n steps.
Return the minimum number of steps required to reach the destination.

Example 1:
Input: target = 3
Output: 2
Explanation:
On the first move we step from 0 to 1.
On the second step we step from 1 to 3.
Example 2:
Input: target = 2
Output: 3
Explanation:
On the first move we step from 0 to 1.
On the second move we step  from 1 to -1.
On the third move we step from -1 to 2.
'''

import math
class Solution:
    def solve(self, A):

        A = abs(A)
        
        n = math.ceil((-1.0 + math.sqrt(1 + 8.0 * A))/2)
        
        summ = n * (n+1) / 2
        if summ == A:
            return n
        
        d = int(summ-A)
        if (d & 1) == 0:
            return n
        else:
            if n & 1:
                return n+2
            return n+1