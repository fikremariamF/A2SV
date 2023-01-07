class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:   
        nums_pos = dict()
        
        for idx, value in enumerate(nums):
            nums_pos[value] = idx
        for value in operations:
            nums[nums_pos[value[0]]] = value[1]
            idx = nums_pos[value[0]]
            del nums_pos[value[0]]
            nums_pos[value[1]] = idx
        return nums
        