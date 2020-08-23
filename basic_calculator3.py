class Solution:
    def calculate(self, s: str) -> int:
        return self.helper(list(s))
    
    def helper(self, s: list):
        if not s:
            return 0
        
        stack = []
        sign = '+'
        num = 0
        
        while s:
            c = s.pop(0)
            
            if c.isdigit():
                num = num*10 + int(c)    
            elif c == '(':
                num = self.helper(s)
            
            
            if not s or (c in ['+', '-', '*', '/', ')']):
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] = stack[-1] * num
                elif sign == '/':
                    stack[-1] = int(stack[-1] / num)
                
                sign = c
                num = 0
                
                if sign == ')':
                    break
                    
        return sum(stack)


if __name__ == "__main__":
    sol = Solution()
    
    testset = [
        '1+3-3*(-1)',
        '23*(44-34)+4*(35-32)'
    ]

    for test in testset:
        print(sol.calculate(test))

