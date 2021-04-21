"""
return great common divisor (GCD) of array

naive Euclidean does not work (TLE)
"""

def generalGCD(arr):
    res = arr[0]
    for x in arr[1:]:
        if res < x:
            res, x = x, res
        
        while x:
            x, res = res % x, x
    
    return res


assert generalGCD([2,4,6,8,10]) == 2