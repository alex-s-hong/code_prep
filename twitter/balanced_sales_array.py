#! usr/bin/env python3
"""
can try with totalsum - cursum - sales[i] == cursum
"""

def balancedSum(sales:list):
    remaining = sum(sales)
    n = len(sales)
    curSum = sales[0]
    remaining -= sales[0]

    for i in range(1, n):
        remaining -= sales[i]
        if remaining == curSum:
            return i 
        curSum += sales[i]





if __name__ == "__main__":
    a1 = [1,2,3,4,6]
    a2 = [1,2,3,3]

    print(balancedSum(a1))
    print(balancedSum(a2))
