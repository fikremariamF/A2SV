class Solution:
    def splitString(self, s: str) -> bool:
        
        prev = None
        
        def split(string):
            nonlocal prev
            if prev and int(prev)== int(string) + 1:
                return True
            
            temp = []
            # print(string, temp)
            for ptr in range(1,len(string)):
                # if prev:
                #     print([string[ :ptr], string[ptr: ]],int(prev),int(string[ :ptr]) + 1)
                if not prev or int(prev) == int(string[ :ptr]) + 1:
                    temp.append([string[ :ptr], string[ptr: ]])
            # print("the Last",string, temp)      
            if not temp:
                return False
            
            for segment in temp:
                prev = segment[0]
                # print("in", prev)
                val = split(segment[1])
                if val == True:
                    return True
                
                
            return False
        
        return split(s)
        
                
            