#! /usr/bin/env python3
import scipy.stats as ss
#import math

T = int(input())

for each_test in range(1, T+1):
    W, H, L, U, R, D = map(int, input().split())
    ans = 0.

    # R=W and D=H, then it can't be reached
    if R != W:
        ans += ss.binom.cdf(U-2, R+U-2, 0.5)
        # for i in range(U-1):
        #     ans += math.factorial(R+U-2)/(math.factorial(i)*math.factorial(R+U-2-i))*0.5**(R+U-2)
    
    if D != H:
        ans += ss.binom.cdf(L-2, L-2+D, 0.5)
        #for i in range(L-1):
        #    ans += math.factorial(L-2+D)/(math.factorial(i) * math.factorial(L-2+D-i))*0.5**(L-2+D)

    print("Case #{}: {}".format(each_test, ans))