"""
list1 = [3,6,4,8]
list2 = [4,6,8,3]

output = 2
(swap 4 with 8, swap 8 with 3)

"""
def minSwapsToSort(arr):
    swaps = 0

    for i,v in enumerate(arr):
        if v == i:
            continue
        else:
            arr[i], arr[v] = arr[v], arr[i]
            swaps +=1

    return swaps

def minSwapToMakeArraySame(list1, list2):
    position2 = {}
    index_list = []

    for i, v in enumerate(list2):
        position2[v] = i

    
    for i, v in enumerate(list1):
        index_list.append(position2[v])
        #list2[i] = position2[v] # put the index in place

    return minSwapsToSort(index_list)
    
print(minSwapToMakeArraySame([3,6,4,8],[4,6,8,3]))
print(minSwapToMakeArraySame([1,2,3,4,5],[2,3,4,1,5]))