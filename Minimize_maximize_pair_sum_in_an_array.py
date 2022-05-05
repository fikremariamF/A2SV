class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        j = len(nums) - 1
        maxsum = 0
        while i < j:
            maxsum = max(maxsum, nums[i] + nums[j])
            i += 1
            j -= 1
        return maxsum
        
