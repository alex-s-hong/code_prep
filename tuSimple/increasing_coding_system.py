"""
26 to decmial

"""

def solver(s:str):
    res = 0
    for i in range(len(s), 0, -1):
        res += (ord(s[i-1]) - 96) * 26**(len(s)-i)

    
    print(res)

solver('a')
solver('ab')