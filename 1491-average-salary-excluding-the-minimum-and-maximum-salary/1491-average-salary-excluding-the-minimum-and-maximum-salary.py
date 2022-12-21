class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        # print(salary)
        sum = 0
        for i in range(1,len(salary)-1):
            print(salary[i])
            sum += salary[i]
        # print(sum)
        # print(len(salary)-2)
        return sum / (len(salary)-2)
            
        