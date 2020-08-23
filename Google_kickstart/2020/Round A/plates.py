#! /usr/bin/env python3
'''
for test in range(int(input())):
    N, K, P = map(int, input().split())
    # last_dp stores the best sum for i plates
    last_dp = [0]*(P+1)
    for i in range(N):
        dp = last_dp
        curr_stack = list(map(int, input().split()))
        cumm = 0
        dp[0] = last_dp[-1]
        for j in range(K):
            cumm += curr_stack[j]
            # pick j plates from curr, P-j from previous
            dp[j+1] = max(dp[j+1], last_dp[P-j-1]+ cumm)
            print(dp)
        last_dp = dp
    print("Case #{}: {}".format(test+1,dp[P]))


'''
for test in range(int(input())):
    n, k, p = map(int, input().split())
    last_dp = [0]*(p+1)
    for i in range(n):
        dp = last_dp[:]
        curr_stack = map(int, input().split())
        s = 0
        for j, x in enumerate(curr_stack):
            s += x
            for l in range(p-j-1, -1, -1):    
                dp[l+j+1] = max(dp[l+j+1], last_dp[l] + s)
        last_dp = dp
    print("Case #{}: {}".format(test+1,dp[p]))

