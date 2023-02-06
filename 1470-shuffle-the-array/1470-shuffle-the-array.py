class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        output = []
        left, right = 0,  len(nums)//2
        
        while right < len(nums):
            output.append(nums[left])
            output.append(nums[right])
            left += 1
            right += 1
        return output