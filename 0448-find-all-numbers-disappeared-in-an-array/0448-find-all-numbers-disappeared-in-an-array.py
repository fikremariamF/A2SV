class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # def quickSort(arr):
        output = []
        # quickSort(nums)
        idx = 0
        while idx < (len(nums)):
            if nums[idx] == nums[nums[idx] - 1]:
                idx += 1
                continue
            if nums[idx] - 1 != idx:
                var = nums[idx] - 1
                nums[var], nums[idx] = nums[idx], nums[var]
            else:
                idx += 1
        for idx in range(len(nums)):
            if nums[idx] - 1 != idx:
                output.append(idx + 1)
        return output