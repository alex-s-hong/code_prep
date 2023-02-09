# https://sites.radford.edu/~nokie/classes/360/dp-rod-cutting.html


def woodcut(p:list, n):
    # given price list for each length (p) and length of the wood (n)
    # find the maximal value
    # R_k = max(P_i, R_k-i) for 1 <= i <= k 
    if n == 0:
        return 0

    revenue = [0] * (n+1)    
    for i in range(1, n+1):
        q = 0
        for j in range(i, -1, -1):
            q = max(q, p[j]+ revenue[i-j])
        revenue[i] = q
    print(revenue)
    return revenue[n]

p = [0,1,5,8,9,10,17,17,20]
print(woodcut(p, 4))
print(woodcut(p, 8))