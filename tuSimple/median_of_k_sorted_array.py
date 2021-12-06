"""
Given K sorted arrays of size N each, find the median of all the arrays.

# Example 1
K = 3
N = 4
Input: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
Output: 6 i.e. (6+7) / 2

# Example 2
K = 3
N = 3
Input: [[10, 100, 1000], [5, 55, 555], [23, 2323, 232323]]
Output: 100
Explanation: All arrays when combined and sorted = [5, 10, 23, 55, 100, 555, 1000, 2323, 232323]. 
Median = 100
"""
def getMedianElement(length):
    if length & 1:
        # odd
        return length // 2, length //2
    else:
        return length // 2 -1, length //2

def getMedian(arr):
    # assume length of each array is same
    total_length = len(arr) * len(arr[0])

    e1, e2 = getMedianElement(total_length)

    counter = 0
    pointer = [0 for _ in range(len(arr))]
    res = [None, None]

    while None in res:
        print(pointer)
        # get actual val
        values = [ arr[i][v] if v < len(arr[i]) else float('inf') for i,v in enumerate(pointer)]
        print('values',values)
        min_val = min(values)
        #max_val = max(values)

        min_val_index = values.index(min_val)
        #max_val_index = values.index(max_val)

        #check if this is the value counter we want
        if counter == e1:
            res[0] = min_val
        if counter == e2:
            res[1] = min_val
        
        pointer[min_val_index] +=1

        counter +=1
    
    return sum(res)/2


inpt = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
#print(getMedian(inpt))

from bisect import bisect_left
from bisect import bisect_right

def kthOfPiles(givenPiles, k, count):
    '''
    Perform binary search for kth element in  multiple sorted list

    parameters
    ==========
    givenPiles  are list of sorted list
    count   is the total number of
    k       is the target index in range [0..count-1]
    '''
    begins = [0 for pile in givenPiles]
    ends = [len(pile) for pile in givenPiles]
    #print('finding k=', k, 'count=', count)
    
    for pileidx,pivotpile in enumerate(givenPiles):
        
        while begins[pileidx] < ends[pileidx]:
            mid = (begins[pileidx]+ends[pileidx])>>1
            midval = pivotpile[mid]
            
            smaller_count = 0
            smaller_right_count = 0
            for pile in givenPiles:
                smaller_count += bisect_left(pile,midval)
                smaller_right_count += bisect_right(pile,midval)
                
            #print('check midval', midval,smaller_count,k,smaller_right_count)
            if smaller_count <= k and k < smaller_right_count:
                return midval
            elif smaller_count > k:
                ends[pileidx] = mid
            else:
                begins[pileidx] = mid+1
            
    return -1

def medianOfPiles(givenPiles,count=None):
    '''
    Find statistical median
    Parameters:
    givenPiles  are list of sorted list
    '''
    if not givenPiles:
        return -1 # cannot find median
    
    if count is None:
        count = 0
        for pile in givenPiles:
            count += len(pile)
            
    # get mid floor
    target_mid = count >> 1
    midval = kthOfPiles(givenPiles, target_mid, count)
    if 0 == (count&1):
        midval += kthOfPiles(givenPiles, target_mid-1, count)
        midval /= 2
        
    return '%.1f' % round(midval,1)

inpt = [[1,3,7,9,11],[2,10,13],[1,2,3,4,5,6],[3,6,9,11]]
print(medianOfPiles(inpt))


"""
pick median from one array, bisect.left to others
sum indexes less than the points (i1, i2, i3,...) and larger than those
if K < sum_less_indexes : check the left
elif K == sum_less_indexes: return the median
else: check the right part (exclude the points)
update K with K- sum_less_indexes
NlogE * Nlog(leverage) => N^2(logE)^2) Kth Smallest in N Sorted
"""
import bisect
def kthSmallest(matrix, k: int) -> int:
        #l, r = matrix[0][0], matrix[-1][-1] # l should be smallest, r would be largest
        l, r = min(arr[0] for arr in matrix), max(arr[-1] for arr in matrix)


        while l < r:
            m = l + (r-l) // 2
            if sum(bisect.bisect(row, m) for row in matrix) < k:
                l = m + 1
            else:
                r= m
        return l
    
print(kthSmallest([[12,13,15],[1,5,9],[10,11,13]], 8))
print(kthSmallest(inpt, 9))
print(kthSmallest(inpt, 10))
print(kthSmallest([[30,122,333],[1,2], [1,2,3]],7))