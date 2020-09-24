'''
https://leetcode.com/problems/sort-colors/
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
Follow up:
Could you solve this problem without using the library's sort function?
Could you come up with a one-pass algorithm using only O(1) constant space?
Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [0,1,2,0,1,2]
Output: [0,0,1,1,2,2]

Example 3:
Input: nums = [0]
Output: [0]
'''

# keep 3 pointers to check -> high = 2, low = 0, mid = 1
# if mid = 0, swap with low then low += 1 & mid += 1
# if mid = 1, mid += 1
# else swap mid with high, high -= 1
class Solution:
    def sortColors(self, arr: List[int]):
    
        n = len(arr)
        low = 0
        high = n-1
        mid = 0
        
        while mid <= high:
            
            if arr[mid] == 0:
                arr[mid], arr[low] = arr[low], arr[mid]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                mid += 1
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1