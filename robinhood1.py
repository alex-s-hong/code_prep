from collections import defaultdict

def contiguous(arr):
    n = len(arr)
    if n < 3: 
        return 0

    total = sum(arr)
    first = 0
    count = 0

    for i in range(n-2):
        first += arr[i]

        # test the rest
        second = 0
        for j in range(i+1, n-1):
            second += arr[j]
            if first <= second and second <= total - first- second:
                count +=1
            elif total - first - second < second:
                break
        
    return count

def oppositesum(arr):
    def rev(integer):
        reverse = 0
        while integer != 0:
            integer, digit = divmod(integer, 10)
            reverse *= 10
            reverse += digit

        return reverse
    
    count_map = defaultdict(int)

    for num in arr:
        count_map[num - rev(num)] += 1
    
    # calculate the combinations of each sum (i <= j)
    ans = 0
    for count in count_map.values():
        ans += count * (count+1) // 2
    
    return ans




if __name__ == "__main__":
    #num = int(input())
    #N = list(map(int, input().split()))

    tests = [[1, 2, 2, 2, 5, 0], [1,1,1], [1,4],[43,12,45,3,0,44, 45]]
    

    for test in tests:
        ans = contiguous(test)
        print(ans)

    
    arr = [1, 20, 2, 11]
    ans2 = oppositesum(arr)
    print(ans2)
    