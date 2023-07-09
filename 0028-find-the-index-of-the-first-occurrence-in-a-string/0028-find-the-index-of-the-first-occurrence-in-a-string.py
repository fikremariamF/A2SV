class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ptr, idx = 0, 0
        while idx < len(haystack):
            if haystack[idx] == needle[ptr]:
                ptr += 1
                idx += 1
            else:
                idx = idx - ptr + 1
                ptr = 0
            if ptr == len(needle):
                return idx - ptr
            
        return -1
        