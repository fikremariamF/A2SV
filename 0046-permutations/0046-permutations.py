class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = set()
        curr = []
        
        def generate(track):
            nonlocal output
            if len(curr) == len(nums) and tuple(curr) not in output:
                output.add(tuple(curr))
                return
            
            for idx in range(len(nums)):
                if (track >> idx) & 1 != 1:
                    newNum = (1 << idx) ^ track
                    curr.append(nums[idx])
                    generate(newNum)
                    curr.pop()
                   
            return
        
        generate(0)
        return list(output)