class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        alphs = [0 for _ in range(26)]
        length = len(s1)
        for letter in s1:
            alphs[ord(letter)-97] += 1
        for i in range(len(s2)- length + 1):
            segment = s2[i:i+length]
            temp_alphs = [0 for _ in range(26)]
            for letter in segment:
                temp_alphs[ord(letter)-97] += 1
            if alphs == temp_alphs:
                return True
        return False
        