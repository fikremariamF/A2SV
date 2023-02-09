class Solution:
    def compare(self,num1, num2):
        num1 = str(num1)
        num2 = str(num2)
        # print(num1 + num2)
        if int(num1 + num2) > int(num2 + num1):
            return 0
        else:
            return 1
    def largestNumber(self, nums: List[int]) -> str:
        for _ in nums:
            for idx in range(len(nums) - 1):
                res = self.compare(nums[idx], nums[idx+1])
                if res:
                    nums[idx], nums[idx+1] = nums[idx + 1], nums[idx]
        for idx in range(len(nums)):
            nums[idx] = str(nums[idx])
        return str(int("".join(nums)))