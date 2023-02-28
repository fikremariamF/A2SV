class Solution:
    def reverse(self, left,right):
        if left < right:
            self.s[left], self.s[right]= self.s[right], self.s[left]
            self.reverse(left +1 , right -1)
        else:
            return
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.s = s
        self.reverse(0, len(s)-1)
        
        