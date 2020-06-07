'''
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
'''
class Solution:

# method 1 - O(n^2) approach
    def findMaxLength(self, nums: List[int]) -> int:
 
        maximum = 0
        
        for i in range(len(nums)):
            count1 = 0
            count2 = 0
            for j in range(i, len(nums)):
                if nums[j] == 0:
                    count1 += 1
                else:
                    count2 += 1
                
                if count1 == count2:
                    maximum = max(maximum, j-i+1)
        
        return maximum
		
# method 2 - O(n) approach with hashmap
# +1 for 1 and -1 for 0 -> and observe pattern -> same value start coming after alternate places 
    def findMaxLength(self, nums: List[int]) -> int:
        
        hashmap = {}
        
        hashmap[0] = -1  # map with count as key and index as changing values
        count = 0
        max_value = 0
        
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count -= 1
            
            if count in hashmap:
                max_value = max(max_value, i - hashmap[count])
            else:
                hashmap[count] = i
        
        return max_value