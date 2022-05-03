class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)-1):
            if nums[i] == (nums[i-1] + nums[i+1])/2:
                value = nums[i+1]
                nums[i+1] = nums[i]
                nums[i] = value
                # print(nums)
                # mybool = True
                if nums[i-1] == (nums[i] + nums[i-2])/2:
                    counter = i
                    while counter > 1:
                        if (nums[counter-2] + nums[counter])/2 == nums[counter-1]:
                            anotherval = nums[counter-1]
                            nums[counter-1] = nums[counter-2]
                            nums[counter-2] = anotherval
                            # print(counter)
                            # print(counter)
                            # print(nums, "with counter")
                        counter -= 1
                        if counter > 2 and (nums[counter-2] + nums[counter])/2 != nums[counter-1] and (nums[counter-3] + nums[counter-1])/2 != nums[counter-2]:
                            break
                        
                
        return nums
        
