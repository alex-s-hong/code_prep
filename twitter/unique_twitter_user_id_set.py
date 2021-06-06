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
    res = 0
    lever = 0
    # lever can be 0 as min number is 1

    for num in sorted(s):
        if lever < num:
            lever = num
        else:
            # duplicate
            lever +=1
            res += lever - num
        res += num
    
    return res






if __name__ == '__main__':
    s = [3,2,1,2,1,7]
    assert getUniqueUserIdSum(s)==22
    s = [3,2,1,4,7]
    assert(getUniqueUserIdSum(s)== 17)
