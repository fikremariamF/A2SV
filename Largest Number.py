class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for n in range(len(nums)):
            nums[n] = str(nums[n])
        for n in range(len(nums)):
            for m in range(len(nums)):
                if nums[n] + nums[m] < nums[m] + nums[n]:
                    nums[n],nums[m] = nums[m], nums[n]
        nums.reverse()
        if int("".join(nums)) == 0:
            return "0"
        else:
            return "".join(nums)
            
