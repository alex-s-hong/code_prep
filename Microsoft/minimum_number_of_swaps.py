"""
Sort the list of integers with minimum number of swaps

 sort it in a way that even numbers are at the start of list in ascending order 
 and the odd numbers are at the end of list in descending order.


O(n**2)
"""
def minimum_number_of_swaps(nums):
    even_count = 0
    odd_count = 0

    for elem in nums:
        if elem & 1:
            odd_count +=1
        else:
            even_count +=1

    swaps = 0

    for i in range(even_count):
        min_even = nums[i] if not nums[i] & 1 else float('inf')
        smallest_index = i
        for j in range(i, len(nums)):
            if not nums[j] & 1 and nums[j] < min_even:
                min_even = nums[j]
                smallest_index = j
        if i != smallest_index:
            nums[i], nums[smallest_index] = nums[smallest_index], nums[i]
            swaps +=1
        
    for i in range(even_count, len(nums)):
        max_odd = nums[i] if nums[i] & 1 else float('-inf')
        largestest_index = i
        for j in range(i, len(nums)):
            if nums[j] & 1 and nums[j] > max_odd:
                max_odd = nums[j]
                largestest_index = j
        if i != largestest_index:
            nums[i], nums[largestest_index] = nums[largestest_index], nums[i]
            swaps +=1

    print(nums)
    return swaps

if __name__ == "__main__":
    nums = [3,2,4,5]
    print(minimum_number_of_swaps(nums))