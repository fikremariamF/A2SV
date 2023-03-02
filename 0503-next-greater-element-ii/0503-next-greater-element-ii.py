class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nextindex = [-1]*len(nums)
        index = []
        limit = len(nums)*2
        limitcounter = 0
        i = 0
        while i < len(nums):
            if len(index) == 0:
                index.append(i)
            else:
                if nums[index[-1]] < nums[i]:
                    while index and nums[index[-1]] < nums[i]:
                        nextindex[index[-1]] = nums[i]
                        index.pop()
                index.append(i)
                if i == len(nums) - 1:
                    i = -1   
                if limitcounter == limit:
                    break
            i += 1
            limitcounter += 1
        return nextindex
