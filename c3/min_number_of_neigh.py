#! usr/bin/env python3
'''
In real world horses neigh, and you can count them by listening to them.

For this problem you will be given an input string consisting of lowercases letters which represents combination of neigh of different horses.

You need to return an integer corresponding to minimum number of distinct horses which can produce the given sequence.

If the input string is not a combination of valid neigh from different horses return -1.


leetcode 1419
'''

def solver(s):
    mark = n = e = i = g = h = 0

    for char in s:
        if char == 'n':
            n += 1
            mark = max(mark, n - h)
        elif char == 'e':
            e += 1
        elif char == 'i':
            i += 1
        elif char == 'g':
            g += 1
        elif char == 'h':
            h += 1
        else:
            return -1
        
        if not n >= e >= i >= g >= h:
            return -1

    if n == h:
        return mark
    else:
        return -1

assert solver('nei') == -1
assert solver("neighneigh") == 1
assert solver("neingeighh") == 2
assert solver("neineigghhneigh") == 2

