class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        minbefore = nums[0]
        for idx in range(1, len(nums)):
            # print(stack, nums[idx])
            while stack and (stack[-1][0] <= nums[idx]):
                stack.pop()
            if stack and stack[-1][1] < nums[idx]:
                    return True
            
            stack.append([nums[idx], minbefore])
            minbefore = min(minbefore, nums[idx])
                        
        return False