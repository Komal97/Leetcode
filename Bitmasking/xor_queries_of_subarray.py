'''
https://leetcode.com/problems/xor-queries-of-a-subarray/
Given the array arr of positive integers and the array queries where queries[i] = [Li, Ri], for each query i compute the XOR of elements from Li to Ri (that is, arr[Li] xor arr[Li+1] xor ... xor arr[Ri] ). Return an array containing the result for the given queries.
Example 1:
Input: arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
Output: [2,7,14,8] 
Explanation: 
The binary representation of the elements in the array are:
1 = 0001 
3 = 0011 
4 = 0100 
8 = 1000 
The XOR values for queries are:
[0,1] = 1 xor 3 = 2 
[1,2] = 3 xor 4 = 7 
[0,3] = 1 xor 3 xor 4 xor 8 = 14 
[3,3] = 8

Example 2:
Input: arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]
Output: [8,0,4,4]
'''

# precompute xor of array
# xor of range (i, j) = precompute[j] ^ precompute[i-1] using the property that same number cancel each other
# so xor of num less than i-1 gets cancel out, and we left with xor of (i, j)
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]):
        
        
        n = len(arr)
        precompute = []
        
        xor = 0
        for num in arr:
            xor ^= num
            precompute.append(xor)
        
        ans = []
        for s, e in queries:
            if s == 0:
                ans += [precompute[e]]
            else:
                ans += [precompute[e] ^ precompute[s-1]]
        
        return ans
            