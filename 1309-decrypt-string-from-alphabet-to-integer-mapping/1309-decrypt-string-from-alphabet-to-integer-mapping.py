class Solution:
    def freqAlphabets(self, s: str) -> str:
        currentNum = []
        returnList = []
        l,r = 0, 0
        while r < len(s):
            # print(l,r)
            if r - l == 2 and s[r] != "#":
                # print("first it")
                currentNum.pop()
                # print("current Num:",currentNum)
                returnList.append(chr(int(currentNum[0])+ 96))
                # print(returnList)
                currentNum = []
                r -= 1
                l = r
            elif s[r] == "#":
                # print("elif")
                # print("current Num:",currentNum)
                returnList.append(chr(int(''.join(currentNum))+ 96))
                # print(returnList)
                currentNum= []
                r += 1
                l = r
            # print(returnList)
            if r < len(s):
                currentNum.append(s[r])
            r += 1
        # print(currentNum)
        if currentNum:
            for value in currentNum:
                returnList.append(chr(int(value)+ 96))

        return ''.join(returnList)
                