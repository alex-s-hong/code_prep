"""
interval scheduling algorithm
"""


def maxEvents(arrival, duration):
    aux = sorted(list(zip(arrival, duration)), key = lambda x: (sum(x), x[1]))

    res, end = 0, -1
    for arr, dur in aux:
        if arr >= end:
            res +=1
            end = arr + dur
    
    return res


print(maxEvents([1, 3, 3, 5, 7], [2, 2, 1, 2, 1])) # 4
print(maxEvents([1, 2], [7, 3])) # 1
print(maxEvents([1, 3, 4, 6], [4, 3, 3, 2])) # 2
print(maxEvents([1,3,15,4,8,12],[2,10,4,3,2,7])) #4



