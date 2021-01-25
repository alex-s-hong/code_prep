#! usr/bin/env python3


def slowestKey(keyTimes):
    #keyTimes = [[chr[k[0]+97],k[1]] for k in keyTimes]
    key, duration = None, 0

    for i in range(len(keyTimes)):
        if i == 0:
            start = 0
        else:
            start = keyTimes[i-1][1]
        
        if keyTimes[i][1]-start > duration:
            duration = keyTimes[i][1] - start
            key = keyTimes[i][0]
    
    return chr(key+97)

        
if __name__ == '__main__':
    print(slowestKey([[0,2], [1,3], [0,7]]))
    print(slowestKey([[0,1],[0,3],[4,5],[5,6],[4,10]]))