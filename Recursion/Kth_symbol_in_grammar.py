'''
https://leetcode.com/problems/k-th-symbol-in-grammar/
On the first row, we write a 0. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

Given row N and index K, return the K-th indexed symbol in row N. (The values of K are 1-indexed.) (1 indexed).

Examples:
Input: N = 1, K = 1
Output: 0

Input: N = 2, K = 1
Output: 0

Input: N = 2, K = 2
Output: 1

Input: N = 4, K = 5
Output: 1

Explanation:
row 1: 0
row 2: 01
row 3: 0110
row 4: 01101001
'''

# first half of every row is same as that of row-1
# second half of every row is same as that of complement of row-1
class Solution:
    def kthGrammar(self, N, K):
        
        if N==1 and K==1:
            return 0
        
        mid = (2**(N-1))//2
        
        if K<=mid:
            return int(self.kthGrammar(N-1, K))
        else:
            return int(not self.kthGrammar(N-1, K-mid))
        


# generate grammar only
def grammar(n, gram):
    if n==1:
        print(gram)
        return

    #print(gram)
    length = len(gram)
    for i in range(length):
        gram += str(int(not(int(gram[i]))))
    grammar(n-1, gram)

grammar(4, '0')