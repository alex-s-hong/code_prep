"""
https://leetcode.com/problems/basic-calculator/
The expression string may contain open ( and closing parentheses ), 
the plus + or minus sign -, non-negative integers and empty spaces .
"""
class Solution2:
    # stack and string reversal

    def evaluate_expr(self, stack):

        res = stack.pop() if stack else 0

        # Evaluate the expression till we get corresponding ')'
        while stack and stack[-1] != ')':
            sign = stack.pop()
            if sign == '+':
                res += stack.pop()
            else:
                res -= stack.pop()
        return res       

    def calculate(self, s: str) -> int:

        stack = []
        n, operand = 0, 0

        for i in range(len(s) - 1, -1, -1):
            ch = s[i]

            if ch.isdigit():

                # Forming the operand - in reverse order.
                operand = (10**n * int(ch)) + operand
                n += 1

            elif ch != " ":
                if n:
                    # Save the operand on the stack
                    # As we encounter some non-digit.
                    stack.append(operand)
                    n, operand = 0, 0

                if ch == '(':         
                    res = self.evaluate_expr(stack)
                    stack.pop()        

                    # Append the evaluated result to the stack.
                    # This result could be of a sub-expression within the parenthesis.
                    stack.append(res)

                # For other non-digits just push onto the stack.
                else:
                    stack.append(ch)

        # Push the last operand to stack, if any.
        if n:
            stack.append(operand)

        # Evaluate any left overs in the stack.
        return self.evaluate_expr(stack)



class Solution:
    # my solution
    def calculate(self, s: str) -> int:
        
        stack = []
        sign = 1
        operand = 0
        res = 0 # so far
        
        for char in s:
            if char.isdigit():
                operand = operand*10 + int(char)
                
            elif char == '+':
                res += sign * operand
                sign = 1
                operand = 0
                
            elif char == '-':
                res += sign * operand
                sign = -1
                operand = 0
                
            elif char == '(':
                """
                e.g. 44 - (5 + 2)
                | - |
                | 44|   5+2)
                -----
                """
                stack.append(res)
                stack.append(sign)
                #reset
                sign = 1
                res = 0
                
            elif char == ')':

                res += sign * operand
                
                res *= stack.pop()
                res += stack.pop()
                
                operand = 0
        
        return res + sign * operand


if __name__ == '__main__':

    s = "1 - (1 - 5)"

    sol = Solution()
    print(sol.calculate(s))
