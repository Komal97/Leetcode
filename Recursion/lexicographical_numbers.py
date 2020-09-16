'''
https://leetcode.com/problems/lexicographical-numbers/
Given an integer n, return 1 - n in lexicographical order.Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.

Input:
n = 13
Output:
[1,10,11,12,13,2,3,4,5,6,7,8,9]
'''

# append 0 to 9 after every digit
class Solution:
    
    def generateLexical(self, i, ans, n):
        if i > n:
            return
        
        ans.append(i)
        for j in range(10):
            self.generateLexical(10*i+j, ans, n)
        
    def lexicalOrder(self, n: int) -> List[int]:
        
        ans = []
        for i in range(1, 10):
            self.generateLexical(i, ans, n)
        return ans 
       