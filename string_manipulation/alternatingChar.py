#!/usr/bin/env python3

import time

class Solution:

    def alternatingCharacters(self, s):
        res = 0
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                res +=1
        
        return res


    def alternatingCharacters_slow(self, s):
        
        ss = list(s)
        i = 1
        res = 0
        while i < len(ss):
            if ss[i] == ss[i-1]:
                del ss[i]
                res +=1
            else:
                i+=1 
        return res


if __name__ == "__main__":
    
    s = Solution()
    start_time = time.time()
    print(s.alternatingCharacters_slow('AAABBBAABB'))
    print("--- %.8f seconds ---" % (time.time() - start_time))
    start_time = time.time()
    print(s.alternatingCharacters('AAABBBAABB'))
    print("--- %.8f seconds ---" % (time.time() - start_time))
