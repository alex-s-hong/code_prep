#! usr/bin/env python3

from itertools import combinations 

# find the number of substring ABC
# sliding window would be faster?



def strangesort(mapping: list, nums: list)-> list:
    dic = {}

    for idx, val in enumerate(mapping):
        dic[val] = idx

    converted = []

    for elem in nums:
        tmp = ""
        for char in elem:
            tmp += str(dic[int(char)])
        converted.append(int(tmp))

    corrected = list(enumerate(converted))
    sorte = sorted(corrected, key= lambda x: x[1])

    res = []
    for x in sorte:
        res.append(nums[x[0]])

    return res



if __name__ == '__main__':
    mapping = [3,5,4,6,2,7,9,8,0,1]
    nums = ['990', '332','32']
    x = strangesort(mapping, nums)
    print(x)