class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in nums:
            i = 0
            while i < len(nums) - 1:
                if nums[i] >= nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                i += 1
        return nums