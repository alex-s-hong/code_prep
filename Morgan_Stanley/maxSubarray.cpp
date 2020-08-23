#include <bits/stdc++.h>
using namepsace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {        
        int sum = 0, smax = INT_MIN;
        for (int num : nums) {
            sum += num;
            cout << smax << ' ' << sum << endl;
            smax = max(smax, sum);
            if (sum < 0) {
                sum = 0;
            }
        }
        return smax;
    }
};

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        return maxSubArray(nums, 0, nums.size() - 1);
    }
private:
    int maxSubArray(vector<int>& nums, int l, int r) {
        if (l == r) 
            return nums[l];
   
        int m = (r + l) / 2, ml = mr = INT_MIN;
        int lmax = maxSubArray(nums, l, m);
        int rmax = maxSubArray(nums, m + 1, r);
        for (int i = m, sum = 0; i >= l; i--) {
            sum += nums[i];
            ml = max(sum, ml);
        }
        for (int i = m + 1, sum = 0; i <= r; i++) {
            sum += nums[i];
            mr = max(sum, mr);
        }

        return max(max(lmax, rmax), ml + mr);
    }
};