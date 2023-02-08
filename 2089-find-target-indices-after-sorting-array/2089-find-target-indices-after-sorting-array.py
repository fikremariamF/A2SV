class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        counter = 0
        new_nums = []
        i = 0
        for value in nums:
            if value < target:
                new_nums.append(value)
        for value in nums:
            if value == target:
                counter = counter + 1
        while counter > 0:
            new_nums.append(target)
            counter = counter - 1
        new_arr = []
        while i < len(new_nums):
            if new_nums[i] == target:
                new_arr.append(i)
            i = i + 1
        return new_arr