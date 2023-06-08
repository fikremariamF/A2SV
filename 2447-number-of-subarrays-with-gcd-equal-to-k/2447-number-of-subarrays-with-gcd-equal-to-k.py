class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count = 0
        
        for i in range(0, len(nums)):
            g = nums[i]
            for j in range(i, len(nums)):
                g = gcd(g,nums[j])
                if g == k: 
                    count += 1
                if g < k: 
                    break
            
        return count