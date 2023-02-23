class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # size = float("inf")
        minSize = len(nums) + 1
        left, right = 0, 0
        total = 0
        while right <= len(nums):
            if total < target and right < len(nums):
                total += nums[right]
                right += 1
            else:
                while total >= target:
                    minSize = min(right-left, minSize)
                    total -= nums[left]
                    left += 1
                if right == len(nums):
                    break
        if minSize > len(nums):
            return 0
        return minSize
                
            