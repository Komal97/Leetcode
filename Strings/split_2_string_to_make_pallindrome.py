'''
https://leetcode.com/problems/split-two-strings-to-make-palindrome/
You are given two strings a and b of the same length. Choose an index and split both strings at the same index, splitting a into two strings: aprefix and asuffix where a = aprefix + asuffix, and splitting b into two strings: bprefix and bsuffix where b = bprefix + bsuffix. Check if aprefix + bsuffix or bprefix + asuffix forms a palindrome.
When you split a string s into sprefix and ssuffix, either ssuffix or sprefix is allowed to be empty. For example, if s = "abc", then "" + "abc", "a" + "bc", "ab" + "c" , and "abc" + "" are valid splits.
Return true if it is possible to form a palindrome string, otherwise return false.
Example 1:
Input: a = "x", b = "y"
Output: true
Explaination: If either a or b are palindromes the answer is true since you can split in the following way:
aprefix = "", asuffix = "x"
bprefix = "", bsuffix = "y"
Then, aprefix + bsuffix = "" + "y" = "y", which is a palindrome.

Example 2:
Input: a = "ulacfd", b = "jizalu"
Output: true
Explaination: Split them at index 3:
aprefix = "ula", asuffix = "cfd"
bprefix = "jiz", bsuffix = "alu"
Then, aprefix + bsuffix = "ula" + "alu" = "ulaalu", which is a palindrome.

Example 3:
Input: a = "xbdef", b = "xecab"
Output: false

Example 4:
Input: a = "zeeea", b = "abcsz"
Output: true
Explaination: Split them at index 4:
aprefix = "zeee", asuffix = "a"
bprefix = "abcs", bsuffix = "z"
Then, aprefix + bsuffix = "zeee" + "z" = "zeeez", which is a palindrome.
'''

# in a = zeeez and b = abxsz
# start from 0 in a, n-1 in b
# match until both characters are matched and after that check string between them pallindrom or not
# here eee is pallindrom so z(a) + eee + z(b)
class Solution:
    
    def checkpallindrome(self, a, i, j):
   
        while i <= j:
            if a[i] != a[j]:
                return False
            i += 1
            j -= 1
        return True
        
    def checkPalindromeFormation(self, a: str, b: str):
        
        n = len(a)

        i = 0
        j = n-1
        
        while i < j and a[i] == b[j]:
            i += 1
            j -= 1
        
        if self.checkpallindrome(a, i, j) or self.checkpallindrome(b, i, j):
            return True
        
        i = 0
        j = n-1
        
        while i < j and b[i] == a[j]:
            i += 1
            j -= 1
            
        if self.checkpallindrome(a, i, j) or self.checkpallindrome(b, i, j):
            return True
        
        return False