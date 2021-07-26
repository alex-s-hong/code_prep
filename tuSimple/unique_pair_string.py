"""
BEDF
1-dist: BE ED DF
2-dist: BD, EF
3-dist: BF

"""

def check_stirng(s:str):
    n = len(s)
    l = list(s)

    for i in range(1,n-1):
        seen = set()
        for j in range(n):
            if j+i < n:
                if (l[j],l[j+i]) in seen:
                    print(l[j],l[j+i])
                    return False
                else:
                    seen.add((l[j],l[j+i]))
            print(seen)
    return True

#print(check_stirng('BEDF'))
#print(check_stirng('GEEFF'))
#print(check_stirng('GEFFE'))
print(check_stirng('EAABEDGCFEG'))