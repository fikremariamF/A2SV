class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i, j = 0, 1
        while j < len(nums):
            if nums[i] == nums[j]:
                nums[i] *= 2
                nums[j] = 0
                i += 2
                j += 2
            else:
                i += 1
                j += 1
        output = [0 for _ in range(len(nums))]
        i = 0
        for val in nums:
            if val != 0:
                output[i] = val
                i += 1
        
        return output