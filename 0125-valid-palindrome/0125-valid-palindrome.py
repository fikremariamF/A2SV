class Solution:
    def isPalindrome(self, s: str) -> bool:
        newlist = []
        for value in s:
            if value.isalpha() or value.isnumeric():
                newlist.append(value.lower())
                
        i,j = 0, len(newlist)-1
        
        while i <= j:
            if newlist[i] == newlist[j]:
                i += 1
                j -= 1
                continue
            else:
                return False
        return True