#!/usr/bin/env python3

from collections import Counter

class Solution:

    def oscillator(self, s: str):
        """
        ascend and descend as a one piece (block),
        if block is not used, call its own
        """
        l = sorted(s)
        
        # initialize
        res = l.pop(0)

        if not l:
            return res
    
        isOs = True
        while l and isOs:
            isOs = False
            i = 0
            # ascend
            while i < len(l):
                if res[-1] < l[i]:
                    res += l.pop(i)
                    isOs = True
                else:
                    i +=1
            # i should be as same as len(l)
            i = len(l) -1
            # descend
            while l and i > -1:
                if res[-1] > l[i]:
                    isOs = True
                    res += l.pop(i)
                i -=1
        if l:
            res += ''.join(l)
            
        return res
        

if __name__ == "__main__":
    s = Solution()
    print (s.oscillator("ababyz"))
    print (s.oscillator("babcbb"))
    print (s.oscillator("zafb"))
    print (s.oscillator("aaazzz"))
