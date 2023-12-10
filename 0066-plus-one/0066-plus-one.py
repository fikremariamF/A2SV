class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits)-1
        flag = False 
        while digits[i] == 9: 
            digits[i] = 0
            if i == 0:
                v = (digits[0]+1)%9
                digits = [0]*(len(digits)+1)
                digits[0] = v
                flag = True 
                break
            i -= 1
        if not flag:
            digits[i] += 1 

        return digits