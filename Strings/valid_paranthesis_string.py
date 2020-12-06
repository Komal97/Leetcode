'''
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:
Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.

Example 1:
Input: "()"
Output: True
Example 2:
Input: "(*)"
Output: True
'''
class Solution:

# method 1
    def checkValidString(self, s: str):
        
        count1 = 0
        count2 = 0
        
        for c in s:
            
            if c == '(':
                count1 += 1
                count2 += 1
            elif c == ')':
                count1 -= 1
                count2 = max(count2 - 1, 0)
            else:
                count1 += 1
                count2 = max(count2 - 1, 0)
                
            if count1 < 0:
                return False
            print(count1, count2)
            
        return count2 == 0
		
# method 2 - input = "*()(())*()(()()((()(()()*)(*(())((((((((()*)(()(*)"
	 def checkValidString(self, s: str):
        
        stack1 = []
        stack2 = []
        n = len(s)
        
        for i in range(len(s)):
            if s[i] == '(':
                stack1.append(i)
            elif s[i] == '*':
                stack2.append(i)
            else:
                if len(stack1) > 0:
                    stack1.pop()
                elif len(stack2) > 0:
                    stack2.pop()
                else:
                    return False
        
        if len(stack1) == 0:
            return True
        elif len(stack1) > 0 and len(stack2) == 0:
            return False
        
        while(len(stack1) > 0 and len(stack2) > 0):
            if stack2[-1] > stack1[-1]:
                stack1.pop()
                stack2.pop()
            else:
                return False