'''
https://leetcode.com/problems/basic-calculator-ii/description/
Given a string s which represents an expression, evaluate this expression and return its value. 
The integer division should truncate toward zero.
You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].
Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example 1:
Input: s = "3+2*2"
Output: 7

Example 2:
Input: s = " 3/2 "
Output: 1

Example 3:
Input: s = " 3+5 / 2 "
Output: 5
 
Constraints:
1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.
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
            if ch.isnumeric():     # if numeric, then push
                if i > 0 and s[i-1].isnumeric():  # this is to form number having multiple digits
                    operands[-1] += ch
                else:
                    operands.append(ch) 
            elif is_operator(ch): 
                # if operator, then pop until precedence of operator in stack if greater or equal
                while len(operators) > 0 and precedence(ch) <= precedence(operators[-1]):
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