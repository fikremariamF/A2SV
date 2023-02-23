class Solution:
    def countarr(self,w): 
        out = [0]*26
        for c in w:
            out[ord(c)-ord('a')]+=1
        return out
    
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        m = len(p)
        p_s = self.countarr(p)
        output = []
        s_s = self.countarr(s[:m])
        
        if s_s == p_s:
            output = [0]
        
        for i in range(1,len(s)-m+1):
            
            left = ord(s[i-1])-ord('a') 
            right = ord(s[i+m-1])-ord('a')
            s_s[left] = s_s[left] -1
            s_s[right] = s_s[right] +1
            
            if s_s == p_s:
                output.append(i)
        return output
                    