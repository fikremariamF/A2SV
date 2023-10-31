class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos = defaultdict(list)
        for i, num in enumerate(nums):
            pos[num].append(i)
        nums.sort()
        left, right = 0, len(nums) - 1
        
        # print(pos)
        while left < right:
            if nums[left] + nums[right] > target:
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                l_pos = pos[nums[left]].pop()
                r_pos = pos[nums[right]].pop()
                return [l_pos, r_pos]        
        