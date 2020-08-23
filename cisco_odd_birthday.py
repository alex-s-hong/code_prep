from collections import defaultdict

def solver(num, N):
    month = defaultdict(int)
    for i in range(num):
        month[N[i]] +=1
    
    res = 0
    for j in month.values():
        if j & 1:
            res +=1
    
    return res


if __name__ == "__main__":
    num = int(input())
    N = list(map(int, input().split()))

    ans = solver(num, N)
    print(ans)