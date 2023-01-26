class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = {}
        
        for index, number in enumerate(sorted(nums)):
            # print(index, ": ", number)
            count.setdefault(number, index)
        # print(count)
        return [count[i] for i in nums]