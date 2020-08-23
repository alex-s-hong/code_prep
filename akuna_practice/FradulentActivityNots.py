#!/usr/bin/env python3

from collections import deque

class CountingSort:

    def __init__(self, d):
        self.trail = [0]* 201 # following constraint
        self.queue = deque()
        self.d_size = d
        self.isOdd = True if d & 1 else False

    def __repr__(self):
        pass
    
    def add(self, val: int):
        self.queue.append(val)
        self.trail[val] += 1
        if len(self.queue) > self.d_size:
            curr = self.queue.popleft()
            self.trail[curr] -=1

    def getMedian(self):  
        cum = 0
        median = None
        med2 = None
        for index, val in enumerate(self.trail):
            cum += val
            if self.d_size // 2 <= cum and median == None:
                #median (low) is found
                median = index
            if self.d_size //2 + 1 <= cum and med2 == None:
                med2 = index
                break
        
        if self.isOdd:
            return med2 
        else:
            #print("med1 = {}, med2 = {}".format(median, med2))
            return (median + med2) / 2.


class Solution:
    # Complete the activityNotifications function below.

    def activityNotifications(self, expenditure, d):

        sorter = CountingSort(d)

        #init
        for elem in expenditure[:d]:
            sorter.add(elem)

        issues = 0

        for elem in expenditure[d:]:
            median = sorter.getMedian()
            print("median is {} and current value is {}".format(median, elem))
            if elem >= median*2:
                issues +=1
            sorter.add(elem)  

        return issues
  

if __name__ == '__main__':

    s = Solution()
        
    res = s.activityNotifications([2,3,4,2,3,6,8,4,5], 5)
    
    print(res)


