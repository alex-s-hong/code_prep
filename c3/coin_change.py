#fewest number of coins that you need to make up that amount
# coins in ascending order
import math

def coinChange(coins, amount):
    # bottom up dp

    dp = [math.inf] * (amount+1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, amount+1):
            dp[x] = min(dp[x], dp[x-coin]+1)
    
    return dp[amount] if dp[amount] != math.inf else -1


print(coinChange([2,3,6],11))
print(coinChange([1,2,5],11))
print(coinChange([2,4],11))
print(coinChange([1],11))
