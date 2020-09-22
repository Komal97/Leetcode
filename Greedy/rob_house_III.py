'''
https://leetcode.com/problems/house-robber-iii/
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.
Determine the maximum amount of money the thief can rob tonight without alerting the police.
Example 1:
Input: [3,2,3,null,3,null,1]
     3
    / \
   2   3
    \   \ 
     3   1

Output: 7 
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:
Input: [2,1,3,null,4]

     2
    / \
   1   3
    \   
     4   

Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 4 = 7
'''

# create pair of inc and exc
# inc =  left.exc + right.exc + root
# exc =  max(left.inc + right.inc, left.exc + right.exc, left.exc + right.inc, left.inc + right.exc)
class Solution:
    class Pair:
        def __init__(self):
            self.inc = 0
            self.exc = 0
            
    def rob(self, root: TreeNode) -> int:
        
        def robHouse(root):
            p = self.Pair()
            if root == None:
                return p

            l = robHouse(root.left)
            r = robHouse(root.right)
            p.inc = l.exc + r.exc + root.val
            p.exc = max(l.inc + r.inc, l.exc + r.exc, l.exc + r.inc, l.inc + r.exc)
            return p
        
        ans = robHouse(root)
        return max(ans.inc, ans.exc)