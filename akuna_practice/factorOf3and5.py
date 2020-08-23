#!/usr/bin/env python3

import time

class Solution:

    def getIdealNums(self, l, r):
        #find the number of ideal integers (3^x * 5^y) within l and r (inclusive)

        # increase by 1, iterate all cases
        count = 0
        for i in range (l, r+1):
            if i & 1 and self.isIdealNum(i):
                print (i)
                count +=1

        return count
            
    def isIdealNum(self, num):
        #even number
        if not num & 1:
            return False
        if num < 2:
            return False
        
        while num > 1:
            if num % 3 == 0:
                num = num // 3

            elif num % 5 ==0:
                num = num // 5
            
            else:
                return False

        return True



if __name__ == "__main__":
    start_time = time.time()
    s = Solution()
    print(s.getIdealNums(200,405))
    print("--- %.8f seconds ---" % (time.time() - start_time))


