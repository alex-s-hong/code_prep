#! usr/bin/env python3

"""
Given an int array and an int target, find how many unique pairs in the array such that their sum is equal to target.
Return the number of pairs.
"""

class Solution:
    
    def __init__(self, nums: list, target: int):
        self.nums = nums
        self.target = target

    def uniquepairs(self):
        dic = {}

        for idx, elem in enumerate(self.nums):
            dic[elem] = idx
        
        pairs = []

        for idx, elem in enumerate(self.nums):
            if self.target - elem in dic and idx != dic[self.target - elem]:
                cur = sorted([elem, self.target-elem])
                if not cur in pairs:
                    pairs.append(cur)
            
        #print(pairs)

        return len(pairs)

    def uniqueTwoSum(self):
        ans, comp = set(), set()
        for n in self.nums:
            c = self.target-n
            if c in comp:
                res = (n, c) if n > c else (c, n)
                ans.add(res)
            comp.add(n)
        return len(ans)

if __name__ == "__main__":
    s1 = Solution([1,1,2,45,46,46], 47)
    print(s1.uniqueTwoSum())

    s2 = Solution([1,1], 2)
    print(s2.uniqueTwoSum())

    s3 = Solution([1,5,1,5], 6)
    print(s3.uniqueTwoSum())