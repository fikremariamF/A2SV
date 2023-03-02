class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_hand = nums
        right_hand = nums[::-1]
        output = []
        
        for idx in range(1,len(nums)):
            left_hand[idx] *= left_hand[idx-1]
        for idx in range(1,len(nums)):
            right_hand[idx] *= right_hand[idx-1]
            
        right_hand.reverse()
        
        output.append(right_hand[1])
        for idx in range(1,len(nums)-1):
            output.append(left_hand[idx-1] * right_hand[idx+1])
        output.append(left_hand[-2])
        return output