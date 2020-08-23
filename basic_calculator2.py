#! /usr/bin/env python3

class Solution:
    def calculate(self, s: str) -> int:
        """
        sign is used as delimiter, and it is evaluated later when new sign comes in.
        last digit has no delimiter, so it should go through same case as when sign is faced.
        """
        s.strip() # enhance the performance
        num = 0
        sign = "+"
        stack = []

        length = len(s)

        for i in range(length):

            if s[i].isdigit():
                num = num * 10 + int(s[i])
            
            if s[i] in "+-/*" or i == length-1:
                # sign is previously set
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                elif sign == "/":
                    stack.append(int(stack.pop() / num)) # should not use // because of banker's rounding
                sign = s[i]
                num = 0

        return sum(stack)

if __name__ == "__main__":
    sol = Solution()
    ans = sol.calculate(input())
    print(ans)