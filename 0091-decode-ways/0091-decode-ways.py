class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        
        def f(s):
            if not s:
                return 1

            ans=0
            
            for i in range(len(s)):
                if i>=2:
                    break
                sub=s[:i+1]
                if sub[0]=="0" or (len(sub)==2 and int(sub)>26):
                    continue
                ans+=f(s[i+1:])
            
            return ans

        return f(s) 