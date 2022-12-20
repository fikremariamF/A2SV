class Solution:
    def similarPairs(self, words: List[str]) -> int:
        mylist = []
        for value in words:
            tempset = set()
            for letter in value:
                tempset.add(letter)
            tempset = list(tempset)
            tempset.sort(key= ord)
            mylist.append(''.join(tempset))
        count = Counter(mylist)
        # print(count)
        sum = 0
        for val in count:
            sum += count[val]*(count[val]-1)//2
        return sum