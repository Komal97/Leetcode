'''
https://leetcode.com/problems/path-sum-iii/
You are given a binary tree in which each node contains an integer value. Find the number of paths that sum to a given value.
The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.
Example:
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:
1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
'''

# same logic of count subarrays with given sum -> consider each as an array
# in preorder, keep totalsum in hashmap and in postorder, remove totalsum from hashmap -> denotes 1 path is finished
from collections import defaultdict
class Solution:
 
    def path(self, root, summ, h, totalsum, count):
        if root == None:
            return
        
        totalsum += root.val
        if totalsum == summ :
            count[0] += 1   
        if (totalsum-summ) in h:
            count[0] += h[totalsum-summ]
        h[totalsum] += 1
        
        self.path(root.left, summ, h, totalsum, count)
        self.path(root.right, summ, h, totalsum, count)

        h[totalsum] -= 1
        if h[totalsum] <= 0:
            del h[totalsum]
        
    def pathSum(self, root: TreeNode, sum: int) -> int:
        
        if root == None:
            return 0
        
        h = defaultdict(int)
        
        totalsum = 0
        count = [0]
        self.path(root, sum, h, totalsum, count)
        return count[0]