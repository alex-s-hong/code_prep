#! /usr/bin/env python3

def solution(N, B):
    N.sort()
    res = 0
    for num in N:
        if num > B:
            return res
        B -= num
        res +=1
    return res

number_of_tests = int(input())
for i in range(number_of_tests):
    _, B = map(int, input().split())
    N = list(map(int, input().split()))
    ans = solution(N, B)
    print("Case #{}: {}".format(i+1, ans))
    
