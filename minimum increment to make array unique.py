class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        counter = 0
        # print(nums)
        for num in range(len(nums)):
            # print("i" , num)
            if num != 0 and nums[num] <= nums[num-1]:
                # print(nums[num], "<=" , nums[num-1])
                counter += nums[num-1] - nums[num] + 1
                nums[num] = nums[num] + nums[num-1] - nums[num] + 1
                # print(nums)
                # print("counter",counter)
        return counter
