#! usr/bin/env python3

def exam(v:list):
    total = 0
    for q in v:
        if q == 1:
            total +=1
        else:
            total -=1
    

    cursum = 0

    for i in range(len(v)):
        if cursum > total:
            return i
        
        cursum += 1 if v[i] == 1 else -1
        total -=1 if v[i] == 1 else -1

    return len(v) # 0 if tied?


if __name__ == '__main__':
    l = [1,0,0,1,0]
    print(exam(l))

    l = [1,1,1,0,1]
    print(exam(l))