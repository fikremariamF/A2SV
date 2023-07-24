class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        def check_subset(nums):
        
            n=len(nums)

            subset=[]
            for i in range(1,2**n):
                b=bin(i)[2:]
                l=len(b)
                subset.append('0'*(n-l)+b)
            return subset

        allsubset=check_subset(nums)

        d={}

        for i in allsubset:
            xor=0
            s=1
            for j in range(len(i)):
                if i[j]=='1' and s==1:
                    xor=int(nums[j])
                    s=0

                if i[j]=='1' and s==0:
                    xor=xor | int(nums[j])

            if xor not in d:
                d[xor]=1
            else:
                d[xor]=d[xor]+1

        mx=sorted(d.keys())[-1]

        return d[mx]