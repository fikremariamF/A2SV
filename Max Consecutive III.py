class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l,r = 0, 0
        longest = 0
        while r < len(nums):
            if nums[r] == 1:
                r += 1
            elif nums[r] == 0 and  k != 0:
                r += 1
                k -= 1
            elif k == 0:
                if nums[l] == 0:
                    k += 1
                l += 1
            if r - l > longest:
                longest = r-l
            
        return longest
