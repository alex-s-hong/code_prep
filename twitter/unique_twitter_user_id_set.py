#! usr/bin/env python3

def getUniqueUserIdSum2(s:list):
    buckets = {}

    elem_sum = 0

    for elem in s:
        elem_sum += elem
        if elem in buckets:
            cur_increment = 1
            cur_elem = elem + 1
            while cur_elem in buckets:
                cur_elem +=1
                cur_increment +=1
            buckets[cur_elem] = True
            elem_sum += cur_increment
        else:
            buckets[elem] = True

    return elem_sum

def getUniqueUserIdSum(s):
    level = 0
    res = 0

    for x in sorted(s):
        if level < x:
            level = x
        else:
            # duplicant 
            level +=1
            res += level - x
        res += x
    
    return res

if __name__ == '__main__':
    s = [3,2,1,2,1,7]
    assert(getUniqueUserIdSum(s)==22)
    s = [3,2,1,4,7]
    assert(getUniqueUserIdSum(s)== 17)
