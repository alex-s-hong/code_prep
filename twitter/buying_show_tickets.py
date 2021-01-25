#! usr/bin/env python3

def time(p:int, tickets:list):
    p = p - 1
    return sum([min(tickets[i], tickets[p]) if i <= p else min(tickets[i], tickets[p]-1) for i in range(len(tickets))])

print(time(2, [5,2,6,3,4,5]))
print(time(4, [5,5,2,3,3]))
print(time(3, [4,5,5,2,3]))
