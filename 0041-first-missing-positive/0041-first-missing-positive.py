class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        maximum = max(nums)
        nums = set(nums)
        for num in range(1,maximum + 5):
            if num not in nums:
                return num
        return 1