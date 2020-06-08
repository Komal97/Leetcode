'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
The replacement must be in-place and use only constant extra memory.
Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n-1
        while(i > 0 and nums[i-1]>=nums[i]):
            i -= 1
            
        if i == 0:
            nums.sort()
            return
        
        if i == n-1:
            nums[i-1], nums[i] = nums[i], nums[i-1]
            return
        
        temp = nums[i-1]
        min_ind = i
        for j in range(i, n):
            if nums[j] > temp and nums[j] < nums[min_ind]:
                min_ind = j
        
        nums[i-1], nums[min_ind] = nums[min_ind], nums[i-1]
        temp = []
        for j in range(i, n):
            temp.append(nums[j])
        temp.sort()
        
        j = 0
        while(i<n):
            nums[i] = temp[j]
            j += 1
            i += 1