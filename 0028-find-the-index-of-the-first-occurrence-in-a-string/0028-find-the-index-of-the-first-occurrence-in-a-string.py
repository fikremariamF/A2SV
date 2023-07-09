class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ptr, idx = 0, 0
        while idx < len(haystack):
            # print(idx, ptr)
            if haystack[idx] == needle[ptr]:
                # print("true")
                ptr += 1
                idx += 1
            else:
                # print("false")
                idx = idx - ptr + 1
                ptr = 0
            if ptr == len(needle):
                # print("found")
                return idx - ptr
            
        return -1
        