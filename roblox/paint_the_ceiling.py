import math, bisect

def variantsCount(n:int, s0: int, k, b, m, a):
    """
    n: number of wall lengths offered
    s0: the length of the shortest wall
    k,b,m: three arbitrary integers
    a: largest area that will be painted for free
    """
    # reusable
    k_mod = k % m
    b_mod = b % m

    wall = [s0]
    i = 1

    while i < n and wall[-1] <= a:
        wall.append(((wall[-1]% m) * k_mod + b_mod) % m + 1 + wall[-1])
        i+=1
    #print(wall)

    sqrt_a = int(math.sqrt(a))
    start = bisect.bisect(wall, sqrt_a)
    count = start ** 2

    # i == len(wall)
    for j in range(start, i):
        limit = a // wall[j]
        count += (bisect.bisect(wall, limit))*2
    
    return count







if __name__ == "__main__":
    ans = variantsCount(3,2,3,3,2,15)
    print(ans)
    ans2 = variantsCount(3,1,1,1,2,4)
    print(ans2)