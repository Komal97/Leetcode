'''
https://leetcode.com/problems/median-of-two-sorted-arrays/
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
Follow up: The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Example 3:
Input: nums1 = [], nums2 = [1]
Output: 1.00000

'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]):
        
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        lengthA = len(nums1)
        lengthB = len(nums2)
        
        low = 0
        high = lengthA
        
        while low <= high:
            
            partitionA = low + (high - low)//2
            partitionB = ((lengthA + lengthB + 1)//2) - partitionA
            
            maxLeftA = nums1[partitionA-1] if partitionA != 0 else float('-inf')
            minRightA = nums1[partitionA] if partitionA < lengthA else float('inf')
            
            maxLeftB = nums2[partitionB-1] if partitionB != 0 else float('-inf')
            minRightB = nums2[partitionB] if partitionB < lengthB else float('inf')
            
            if maxLeftA <= minRightB and maxLeftB <= minRightA:
                if (lengthA + lengthB) & 1:
                    return max(maxLeftA, maxLeftB)
                else:
                    return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB))/2
            elif maxLeftA > minRightB:
                high = partitionA - 1
            else:
                low = partitionA + 1