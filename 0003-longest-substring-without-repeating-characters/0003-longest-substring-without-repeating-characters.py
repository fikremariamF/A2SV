class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        value_set=[]
        l, r = 0, 0
        max_len = 0
        while r < len(s):
            if s[r] not in value_set:
                value_set.append(s[r])
                r += 1
            else:
                value_set.remove(s[l])
                l += 1
            if max_len < r- l:
                max_len = r - l
        return max_len
                
                