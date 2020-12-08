'''
https://leetcode.com/problems/valid-parenthesis-string/
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
        
        count1 = 0  # this works according ( and tells about )
        count2 = 0  # this works according ) and tells about (
        
        for c in s:
            
            if c == '(':
                count1 += 1
                count2 += 1
            
            # there is no effect if count2 become -ve because count1 itself tell everything on becoming -ve
            elif c == ')':
                count1 -= 1
                count2 = max(count2 - 1, 0)
                
            else:
                # consider * as ( in count1 and as ) in count2
                count1 += 1
                count2 = max(count2 - 1, 0)
            
            # if count1 becomes -ve means ) is extra
            if count1 < 0:
                return False
            print(count1, count2)
        
        # if count2 remains +ve means ( is extra
        return count2 == 0
		
# method 2 - input = "*()(())*()(()()((()(()()*)(*(())((((((((()*)(()(*)"
	 def checkValidString(self, s: str):
        
        stack1 = []
        stack2 = []
        n = len(s)
        
        for i in range(len(s)):
            
            # push ( in first stack
            if s[i] == '(':
                stack1.append(i)
                
            # push * in second stack
            elif s[i] == '*':
                stack2.append(i)
                
            # if ) encountered
            else:
                # then pop equivalent ( from first stack
                if len(stack1) > 0:
                    stack1.pop()
                # if no ( then pop *  
                elif len(stack2) > 0:
                    stack2.pop()
                # if ( and * are not available means ) is extra
                else:
                    return False
        
        # if string finish and no open bracket means balanced string
        if len(stack1) == 0:
            return True

        # if string finish and ( remaining then invalid
        elif len(stack1) > 0 and len(stack2) == 0:
            return False
        
        # if string finish and characters left in ( and * stack then make them equal
        while(len(stack1) > 0 and len(stack2) > 0):
            
            # if * occur after ( only then they form pair
            if stack2[-1] > stack1[-1]:
                stack1.pop()
                stack2.pop()
            else:
                return False