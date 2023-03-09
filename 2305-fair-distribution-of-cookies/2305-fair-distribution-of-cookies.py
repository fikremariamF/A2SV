class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        if k == len(cookies):
            return max(cookies)
        minimum = float("inf")
        def distribute(arr,ptr):
            nonlocal minimum
            if ptr == len(cookies):
                minimum = min(max(arr), minimum)
                return

            for idx in range(len(arr)):
                temp = arr[:]
                temp[idx] += cookies[ptr]
                distribute(temp, ptr+1)
            return

        distribute([0 for _ in range(k)], 0)
        return minimum