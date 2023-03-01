class Solution:
    def find_max_score(self, turn, left, right):
        if left < right:
            first_case = self.nums[left] - self.find_max_score(False,left + 1, right)
            second_case = self.nums[right] - self.find_max_score(False,left, right - 1)
            # print("my turn", first_case, second_case)
            return max(first_case, second_case)
        else:
            return self.nums[left]
                
    def PredictTheWinner(self, nums: List[int]) -> bool:
        self.nums = nums[:]
        score = 0
        if len(nums) == 1:
            return True
        else:
            score += self.find_max_score(True, 0, len(nums) - 1)
            # print(score)
        # player2 = sum(nums) - score
        if 0 > score:
            return False
        return True