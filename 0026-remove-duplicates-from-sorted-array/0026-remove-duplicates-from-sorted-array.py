class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr = 1
        prev = nums[0]
        while ptr < len(nums):
            if nums[ptr] == prev:
                prev = nums[ptr]
                nums[ptr] = "_"
            else:
                prev = nums[ptr]
            ptr += 1
        ptr_left = 0
        ptr_right = 1
        while ptr_right < len(nums) - 1:
            while ptr_right < len(nums) - 1 and nums[ptr_right] == "_":
                ptr_right += 1
            while nums[ptr_left] != "_" and ptr_left < ptr_right:
                ptr_left += 1
            if nums[ptr_left] == "_" and nums[ptr_right] != "_":
                nums[ptr_left], nums[ptr_right] = nums[ptr_right], nums[ptr_left]
            elif ptr_left == ptr_right:
                if ptr_right < len(nums) - 1:
                    ptr_right += 1
            else:
                break
        counter = 0
        for num in nums:
            if num != "_":
                counter += 1
        return counter