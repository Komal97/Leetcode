'''
https://www.geeksforgeeks.org/problems/segregate-0s-and-1s5106/1
Given an array of length n consisting of only 0's and 1's in random order. Modify the array in-place to segregate 0s on the left side and 1s on the right side of the array.

Example 1:
Input:
n = 5
arr[] = {0, 0, 1, 1, 0}
Output: {0, 0, 0, 1, 1}
Explanation: 
After segregate all 0's on the left and 1's on the right modify array will be {0, 0, 0, 1, 1}.

Example 2:
Input:
n = 4
arr[] = {1, 1, 1, 1}
Output: {1, 1, 1, 1}
Explanation: There are no 0 in the given array, so the modified array is 1 1 1 1.
'''

# use partition method of quick sort to move 0 on left and 1 on right side
class Solution:
    def segregate0and1(self, arr, n):
        
        pivot = 0
        i = 0
        j = 0
        
        while j < n:
            if arr[j] == pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j += 1
            else:
                j += 1