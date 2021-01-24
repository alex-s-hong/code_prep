#! usr/bin/env python3

from collections import Counter

def getMinimumDifference(n: int, a:list, b:list):
    res = []

    for i in range(n):
        if len(a[i]) != len(b[i]):
            res.append(-1)
        
        else:
            dic = Counter(a[i])
            count = 0

            for elem in b[i]:
                if elem in dic:
                    if dic[elem]:
                        dic[elem] -=1
                    else:
                        count +=1
                else:
                    count +=1
            
            res.append(count)

    return res
                
if __name__ == '__main__':
    a = ['a','jk', 'abb', 'mn', 'abc']
    b = ['bb','kj', 'bbc', 'op', 'def']

    print(getMinimumDifference(5, a, b))