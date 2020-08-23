#! /usr/bin/env python3

t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
    N = int(input())
    if N < 3:
        print("Case #{}: 0".format(i))
        _ = input()
    else:
        
        heights = list(map(int, input().split())) # make input of integers to list of the integers
        peaks = 0
        j = 1
        while j < len(heights)-1:
            if heights[j] > heights[j-1] and heights[j] > heights[j+1]:
                peaks +=1
                j +=2
            else:
                j +=1
        
        print("Case #{}: {}".format(i, peaks))
        