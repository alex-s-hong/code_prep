class Solution:
    def findKthLargest(self, nums: list, k: int) -> int:
        return self.kthLargestHelper(nums, 0, len(nums)-1,  len(nums)-k)

    
    def partition(self, nums, l, r, pivot):
        pivot_val = nums[pivot]
        # 1. move elem to end
        nums[pivot], nums[r] = nums[r], nums[pivot]
        
        index = l
        for i in range(l, r):
            if nums[i] < pivot_val:
                nums[index], nums[i] = nums[i], nums[index]
                index += 1
        
        #3. move pivot to the final place
        nums[r], nums[index] = nums[index], nums[r]
        
        return index
    
        
    def kthLargestHelper(self, nums, l, r, k):
        if l == r:
            return nums[l]
        
        pivot = (l+r)//2 
        
        pivot = self.partition(nums, l, r, pivot)
        
        if k == pivot:
            return nums[k]
        
        elif k < pivot:
            return self.kthLargestHelper(nums, l, pivot-1, k)
        else:
            return self.kthLargestHelper(nums, pivot+1, r, k)
       

s = Solution()
assert(s.findKthLargest([-1,2,0], 2) == 0)
assert(s.findKthLargest([-99,-99], 1) == -99) 
assert(s.findKthLargest([3,2,3,1,2,4,5,5,6],4)==4)