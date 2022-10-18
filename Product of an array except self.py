class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = 1
        counter = 0
        for num in nums:
            if num != 0:
                ans = ans * num
            else:
                counter += 1
            # print(counter)
        if counter == 1:
            for num in range(0,len(nums)):
                if nums[num] == 0:
                    nums[num] = ans
                else:
                    nums[num] = 0
            print(nums)
            return nums
        elif counter > 1:
            for num in range(0,len(nums)):
                nums[num] = 0 
            return nums
                    
        for value in range(0,len(nums)):
            if nums[value] != 0:
                nums[value] = ans//nums[value]
            else:
                nums[value] = ans
        return nums
