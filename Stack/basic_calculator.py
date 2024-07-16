'''
https://leetcode.com/problems/basic-calculator/description/
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.
Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example 1:
Input: s = "1 + 1"
Output: 2

Example 2:
Input: s = " 2-1 + 2 "
Output: 3

Example 3:
Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
 
Constraints:
1 <= s.length <= 3 * 105
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
'+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
'-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
There will be no two consecutive operators in the input.
Every number and running calculation will fit in a signed 32-bit integer.
'''

class Solution:
    def calculate(self, s: str) -> int:
        def precedence(ch):
            if ch == "*" or ch == '/':
                return 2
            elif ch == '+' or ch == '-':
                return 1
            return 0
        
        def calc(a, b, op):
            a = int(a)
            b = int(b)
            if op == '+':
                return a + b
            elif op == '-':
                return a - b
            elif op == '*':
                return a * b
            else:
                return a//b
        
        def is_operator(ch):
            return ch == '+' or ch == '-' or ch == '*' or ch == '/'

        operands = [] 
        operators = []

        for i in range(len(s)):
            ch = s[i]
            if ch == ' ':
                continue

            if ch == '(':                           # if opening bracket, then directly push
                operators.append(ch)
            elif ch.isnumeric():                    # if numeric, then push
                if i > 0 and s[i-1].isnumeric():    # this is to form number having multiple digits
                    operands[-1] += ch
                else:
                    operands.append(ch) 
            elif ch == ')': 
                # pop and evaluate suntil opening bracket is found
                while operators[-1] != '(':
                    op = operators.pop()
                    b = operands.pop()
                    a = operands.pop()
                    val = calc(a, b, op)
                    operands.append(val)
                operators.pop() # pop opening bracket
            elif is_operator(ch):
                # if operator, then pop until precedence of operator in stack if greater/equal or top is opening bracket
                while len(operators) > 0 and operators[-1] != '(' and precedence(ch) <= precedence(operators[-1]):
                    op = operators.pop()
                    b = operands.pop()
                    a = operands.pop()
                    val = calc(a, b, op)
                    operands.append(val)
                operators.append(ch)

        # evaluate whole left expression       
        while len(operators) > 0:
            op = operators.pop()
            b = operands.pop()
            a = operands.pop()
            val = calc(a, b, op)
            operands.append(val)
        
        return int(operands[-1])

        