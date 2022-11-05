class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l , r = 0, 0
        total = nums[r]
        difference = 0
        
        while r < len(nums):
            if total + k >= nums[r] * (r - l + 1):
                difference = max(difference, r-l + 1)
                r += 1
                if r < len(nums):
                    total += nums[r]
            else:
                total -= nums[l]
                l += 1
            
        return difference
