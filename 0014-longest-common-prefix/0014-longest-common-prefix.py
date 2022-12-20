class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = len(strs[0])
        for i in strs:
            if len(i) <= length:
                length = len(i)
        mylist = []
        for i in range(length):
            letter = None
            for n in range(len(strs)):
                if strs[n] == strs[0]:
                    letter = strs[n][i]
                if letter == strs[n][i]:
                    # print(letter)
                    if n == len(strs)-1:
                        mylist.append(letter)
                    continue
                else:
                    return "".join(mylist)
        return "".join(mylist)
                        
            
            
        