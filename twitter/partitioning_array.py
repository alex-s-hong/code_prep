#! usr/bin/env python3

"""
1. each element in the array occurs in exactly one subsequence 중복 사용 안됨
2. all the numbers in a subsequence are distinct 같은 숫자 중복 안됨
3. elements in the array having the same value must be in different subsequences 같은 숫자 등장시 다른 서브셋에 등장해야함
"""
from collections import Counter

def solve(k:int, numbers:list):
    if k == 0 or not numbers:
        return "YES"

    n = len(numbers)

    if n %k != 0:
        return "NO"
    
    counter = Counter(numbers)

    for entry in counter:
        if counter[entry] > n/k:
            return "NO"
    return "YES"


if __name__ == '__main__':
    assert(solve(2,[1,2,3,4])=='YES') #yes
    assert(solve(2,[1,2,3,3])=='YES') #yes
    print(solve(3,[1,2,3,4])) #no
    print(solve(3,[3,3,3,6,6,6,8,9,9]))#yes
    print(solve(1,[]))#yes
    print(solve(1,[1]))#yes
    print(solve(2,[1,2]))#yes


