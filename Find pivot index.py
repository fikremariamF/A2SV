class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        start = 0
        for n in range(0,len(nums)):
            end = total - nums[n] - start
            if start == end:
                return n
            start += nums[n]
        return -1
            
