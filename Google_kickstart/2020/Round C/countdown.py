#! /usr/bin/env python3

T = int(input())

for i in range(1, T+1):
    N, K = map(int, input().split())
    num = list(map(int,input().split()))

    res = 0
    curr = 0
    prev  = None
    for j in range(N):
        if j == 0:
            curr = 1
            prev = num[j]
        else:
            if num[j] == prev - 1:
                curr +=1
            else:
                if curr >= K and prev == 1:
                    res += 1

                curr = 1
            prev = num[j]
    if curr >= K and prev == 1:
        res += 1
    
    
    print("Case #{}: {}".format(i, res))