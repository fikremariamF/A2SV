class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pt_left, pt_right = 0, 1
        
        positives = []
        negatives = []
        for value in nums:
            if value > 0:
                positives.append(value)
            else:
                negatives.append(value)
        nums = []
        for index in range(len(positives)):
            nums.append(positives[index])
            nums.append(negatives[index])
        return nums