def maximize_yield_from_sheet(width, height, values):
    #   '''
    #   Suppose you find a piece of sheet metal that is `width` inches
    #   wide, and `height` inches tall. You would like to sell this sheet 
    #   metal to make as much money as you can. Unfortunately, there
    #   are some rather strict rules regulating sheet metal sales in your
    #   country:
    #     Rule 1) All sheet metal must be sold in squares.
    #     Rule 2) All sheet metal must have integer-length sides.
    
    
    #   Fortunately, you own a tool that you can use to cut your sheet
    #   metal. This tool has a couple rules of its own:
    #     Rule 1) Your tool can only make straight line cuts in the
    #       horizontal or vertical direction (no diagonal cuts).
    #     Rule 2) Once a cut has begun, it must continue all the
    #       way to the end of the sheet. As a result, 1 cut makes 2 sheets.
    #     Rule 3) This tool can only cut 1 sheet at a time.
    
    #   Finally, it is worth noting that the market for sheet metal is not
    #   very rational; the price for a square of sheet metal is in no way
    #   proportional to its size (a smaller square may be worth more 
    #   then a larger one). Implement this function to return the maximum
    #   value which can be obtained by cutting your sheet metal into 
    #   squares, and selling these squares. 
    
    #   width: int, width of sheet of metal
    #   height: int, height of width of metal
    #   values: list<float>: values[n] is the market value of a square of sheet
    #        metal with side length n. Values[0] is 0. len(values) >> max(width, height)
    #   returns: float, maximum value which can be attained by slicing this 
    #       sheet into squares to be sold.
    
    #   Example: maximize_yield_from_sheet(2, 2, [0, 1, 3, 4]) returns 4 (4 1x1 squares)
    #   Example: maximize_yield_from_sheet(2, 2, [0, 1, 5, 6]) returns 5 (1 2x2 square)
    #   Example: maximize_yield_from_sheet(3, 2, [0, 1, 5, 6]) returns 7 (1 2x2 square, 2 1x1 squares)
    #   Example: maximize_yield_from_sheet(4, 4, [0, 0.5, 3.9, 9, 0]) returns 15.6 (4 2x2 squares)
    #   Example: maximize_yield_from_sheet(3, 4, [0, 0, 10, 1, 0]) returns 20 (2 2x2 squares, 4 1x1 squares) 
    #   '''

    if width == 0 or height == 0:
        return 0
    
    width, height = max(width,height), min(width, height)

    dp = [[0 for _ in range(width+1)] for _ in range(height+1)]
    dp[1][1] = values[1]


    for i in range(1,height+1):
        for j in range(1,width+1):
            q = 0
            for k in range(min(i,j)+1):
                q = max(q, values[k] + dp[i-k][k] + dp[k][j-k] + dp[i-k][j-k])
            dp[i][j] = q

            if j <= height and i <= width:
                dp[j][i] = q

    print(dp)
    return dp[height][width]

assert maximize_yield_from_sheet(2, 2, [0, 1, 3, 4]) == 4
assert maximize_yield_from_sheet(2, 2, [0, 1, 5, 6]) == 5
assert maximize_yield_from_sheet(3,2,[0,1,5,6]) == 7
assert maximize_yield_from_sheet(4, 4, [0, 0.5, 3.9, 9, 0]) == 15.6
assert maximize_yield_from_sheet(3, 4, [0, 0, 10, 1, 0]) == 20