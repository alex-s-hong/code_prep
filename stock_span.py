#!/usr/bin/env python3
"""
The span Si of the stock’s price on a given day i is defined as the maximum number of consecutive days just before the given day, 
for which the price of the stock on the day is less than or equal to its price on the given day.
// other definition
The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backwards) 
for which the price of the stock was less than or equal to today's price.

"""


class Solution:

    def stock_span(self, prices):
        span = [None for i in range(len(prices)+1)] #return this

        # the first day's span should be 1.
        span[0] = 1

        stack = []

        for i in range(len(prices)):

            while stack and prices[stack[-1]] <= prices[i]:
                stack.pop()
            
            span[i] = i - stack[-1] if stack else i + 1
        
            stack.append(i)

        return span[:-1]




if __name__ == "__main__":
    s = Solution()
    prices = [100, 80, 60, 70, 60, 75, 85]
    ans = s.stock_span(prices)
    print(*ans)
    '''
    t = int(input())
    
    for i in range(t):
        numL = input() 
        prices = list(map(int, input().split()))
        spans = s.stock_span(prices)
        print(*spans)
    '''