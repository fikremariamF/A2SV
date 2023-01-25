class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        length = len(nums)
        for idx in range(len(nums)):
            nums.append(int((str(nums[idx]))[::-1]))
        return len(set(nums))