'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''

class Solution:

#method - 1
    def square_num(self, n):
        nsum = 0
        num = 0
        while(n>0):
            num = int(n%10)
            nsum = nsum + num**2
            n = int(n/10)
        return nsum
    
    def isHappy(self, n: int) -> bool:
        n_set = set()
        while True:
            n = self.square_num(n)
            if n == 1:
                return True
            elif n in n_set:
                return False
            else:
                n_set.add(n)
				
#method - 2
	def numSquareSum(self, n): 
        squareSum = 0
        while(n): 
            squareSum += (n % 10) * (n % 10)
            n = int(n / 10)
        return squareSum
    
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = n 
        while(True): 

            slow = self.numSquareSum(slow)

            fast = self.numSquareSum(self.numSquareSum(fast)) 
            if(slow != fast): 
                continue; 
            else: 
                break; 

        return (slow == 1); 