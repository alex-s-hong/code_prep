#! /usr/bin/env python3

from itertools import combinations 

# find the number of substring ABC
# sliding window would be faster?



def analyzeInvestment(s: str):
    res = [s[x:y] for x, y in combinations(range(len(s) + 1), r = 2) if 'A' in s[x:y] and 'B' in s[x:y] and 'C' in s[x:y]] 
    return len(res)


if __name__ == '__main__':
    a = 'ABCDXABDFKEABDCKKBKCDADDBABFBA'
    x = analyzeInvestment(a)
    print(x)