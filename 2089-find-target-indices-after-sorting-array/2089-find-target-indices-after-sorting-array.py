class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        output = []
        for index in range(len(nums)):
            if nums[index] == target:
                output.append(index)
        return output