class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        output = [0 for i in range(len(nums))]
        for index in range(len(nums)):
            output[index] = nums[nums[index]]
        return output