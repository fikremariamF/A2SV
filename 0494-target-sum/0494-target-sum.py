from functools import cache          
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @cache
        def dp(curr, idx):
            if idx == len(nums) and curr == target:
                return 1
            
            if idx >= len(nums):
                return 0
            
            ans = dp(curr + nums[idx], idx + 1)
            ans += dp(curr - nums[idx], idx + 1)
                
            return ans
        
        return dp(0, 0)
            
            
            