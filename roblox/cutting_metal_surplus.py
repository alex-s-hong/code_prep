def maxProfit(costPerCut:int, salePrice:int, lengths:list):
    def helper(unit_size):
        gross = 0
        for length in lengths:
            cuts, left = divmod(length, unit_size)
            profit = (cuts * salePrice * unit_size) - cuts * costPerCut

            if not left:
                profit += costPerCut
            
            if profit > 0:
                gross += profit

        return gross

    maxlen = max(lengths)
    res = 0

    for i in range(1, maxlen+1):
        res = max(res, helper(i))
    return res

output = 1770
assert maxProfit(1, 10, [26, 103, 59]) == output

output = 1230
assert maxProfit(100, 10, [26, 103, 59]) == output


