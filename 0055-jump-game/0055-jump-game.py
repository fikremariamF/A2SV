class Solution:
    def canJump(self, nums: List[int]) -> bool:
        stack = [0]
        visited = set()
        
        while stack:
            # print(stack)
            popped = stack.pop()
            if popped == len(nums) - 1:
                return True
            visited.add(popped)
            for num in range(nums[popped]+1):
                step = popped + num
                if step not in visited and step < len(nums):
                    stack.append(step)
        return False