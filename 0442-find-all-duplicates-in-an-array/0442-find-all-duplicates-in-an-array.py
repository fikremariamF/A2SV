class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        output = []
        idx = 0
        while idx < (len(nums)):
            if nums[idx] == nums[nums[idx] - 1]:
                # output.append(nums[idx])
                idx += 1
                continue
            if nums[idx] - 1 != idx:
                var = nums[idx] - 1
                nums[var], nums[idx] = nums[idx], nums[var]
            else:
                idx += 1
        # print(nums)
        for idx in range(len(nums)):
            if nums[idx] - 1 != idx:
                output.append(nums[idx])
        return output