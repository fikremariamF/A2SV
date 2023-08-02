class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()

        count = 0
        curr_num = nums[0]

        for i in nums[1:]:
            if(i == curr_num):
                count += 1
            elif(count == 2):
                count = 0
                curr_num = i

            else:
                return curr_num
        return curr_num