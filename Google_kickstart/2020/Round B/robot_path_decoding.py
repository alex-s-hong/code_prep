#! /usr/bin/env python3

N = 10**9

T = int(input())

for each_test in range(1, T+1):
    instruction = input()

    cur = [0,0]

    stack = []

    for c in instruction:
        if c == 'N':
            cur[0] -=1
        elif c == 'S':
            cur[0] +=1
        elif c == 'W':
            cur[1] -=1
        elif c == 'E':
            cur[1] +=1
        
        # number is between 2 and 9, no need to worry on number bigger than 9
        elif c.isdigit():
            stack.append((cur[0], cur[1], int(c)))
        
        elif c == '(':
            cur = [0,0]
        elif c == ')':
            tmp_w, tmp_h, mul = stack.pop()
            cur[0], cur[1] = tmp_w + mul*cur[0], tmp_h + mul*cur[1]
        
    lat = (cur[0]+1) % N
    if lat == 0: lat = N

    lon = (cur[1]+1) % N
    if lon == 0: lon = N
    
    print("Case #{}: {} {}".format(each_test, lon, lat))
    