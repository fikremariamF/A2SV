class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        lenNums = len(nums)
        nums = set(nums)
        for i in range(len(nums) + 1):
            if i not in nums:
                return i
    
        