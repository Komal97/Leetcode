class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A == 1:
            return 1
        count = 1
        length = 1
        while count < A:
            length += 1
            elcount = (1<<(length-1))//2
            count += elcount
        count -= ((1<<(length-1))//2)
        
        offset = A-count-1
        ans = (1<<(length-1))
        ans |= (offset << (length//2))
        valforrev = (ans>>(length//2))
        rev = 0
        while valforrev:
            rev <<= 1
            rev |= (valforrev&1)
            valforrev >>= 1
        
        ans |= rev
        return ans
            
            
            