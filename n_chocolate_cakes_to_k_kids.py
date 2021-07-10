"""
3 bowls 6 kids

[3, 2, 1]
-> [1,1,1,1,1,1]

calories : each intake ^2

[19], 4
[5,5,5,4]

20 bowls, 40 kids


10
3
3 3 4

8 
3
3 3 2

19
4
4 4 4 4

"""
def k_kids_distribute(n_bowls:list, k_kids:int):
    total_cakes = sum(n_bowls)
    if total_cakes % k_kids == 0:
        return (total_cakes // k_kids)**2 * k_kids
    
    else:
        each, mod = divmod(total_cakes, k_kids)
        return (each+1)**2 * mod + each**2 * (k_kids-mod)


#print(k_kids_distribute([3,2,1],6)) # 6
#print(k_kids_distribute([19],4)) # 19

def mergeSort(arr):
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
 
        # into 2 halves
        R = arr[mid:]
 
        # Sorting the first half
        mergeSort(L)
 
        # Sorting the second half
        mergeSort(R)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

mer = [12,11,5,6,7]
mergeSort(mer)
print(mer)