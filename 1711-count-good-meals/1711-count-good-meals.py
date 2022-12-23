class Solution:
    
    def checker(self, mealValue, powers, mealDict):
        pair = 0
        for power in powers:
            difference = power - mealValue
            if difference in mealDict.keys():
                if mealValue == difference:
                    pair += mealDict[mealValue] - 1
                else:
                    pair += mealDict[difference] 
        return pair
    
    def countPairs(self, given: List[int]) -> int:
        
        pairs = 0
        mealDict = Counter(given)
        
        twos_powers = []
        for number in range(0,22):
            twos_powers.append(2 ** number)
        for value in given:
            pairs += self.checker(value, twos_powers, mealDict)
            # self.checked.add(value)
        pairs = pairs // 2
        
        return pairs % ((10**9) + 7)
        