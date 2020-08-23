#! /usr/bin/env/ python3

def partition(arr, l, r):
    pivot  = arr[r]

    i = l -1

    for j in range(l, r):
        if arr[j] < pivot:
            i +=1
            arr[i], arr[j] = arr[j], arr[i]
            print(arr)

    arr[i+1], arr[r] = arr[r], arr[i+1]

    return i+1

if __name__ == "__main__":
    s = [30, 20, 40, 70, 10, 80, 100, 50]
    res = partition(s, 0, len(s)-1) 
    print(res)

