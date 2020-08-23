#! /usr/bin/env python3

t = int(input()) # number of tests
for each_test in range(1, t + 1):
    lenN, D = map(int, input().split())
    
    N = list(map(int, input().split()))
    
    N = N[::-1]
    pre_max = D
    
    for i in range(lenN):
        n = pre_max // N[i]
        pre_max = n*N[i]
        
    print("Case #{}: {}".format(each_test, pre_max))
