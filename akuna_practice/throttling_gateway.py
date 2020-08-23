#!/usr/bin/env python3
"""
constraint: maximum 3 requests a second,
max 10 requests in 10 sec
max 60 requests in 60 sec
"""

def  dropped_request(r_time: list)->int:
    """
    returns the number of dropped requests
    """
    dic = {}
    for elem in r_time:
        if elem in dic:
            dic[elem] += 1
        else:
            dic[elem] = 1

    time = [i for i in dic]
    time.sort()
    res = 0
    for sec in time:
        res += max(0, dic[sec]-3)
        res += max(0, sum(dic[s] for s in range(max(min(time), sec - 9),sec + 1) if s in dic) - 20)
        res += max(0, sum(dic[s] for s in range(max(min(time), sec - 59), sec + 1) if s in dic) - 60)
    return res

if __name__ == '__main__':
    REQUEST = [1, 1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 11, 11, 11, 6, 6, 6, 5, 5, 5]
    print(dropped_request(REQUEST))
    