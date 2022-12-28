class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        s_window = sum(arr[:k])
        
        if (s_window / k) >= threshold:
            count += 1
        
        for end in range(k, len(arr)):
            s_window += arr[end] - arr[end - k]
            
            if (s_window / k) >= threshold:
                count += 1
        
        return count