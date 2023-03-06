class Solution:
    def findFrequency(self,word):
        minimum = min(word)
        
        count = 0
        for letter in word:
            if letter == minimum:
                count += 1
        return count
    
    
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        for idx in range(len(queries)):
            queries[idx] = self.findFrequency(queries[idx])
            
        for idx in range(len(words)):
            words[idx] = self.findFrequency(words[idx])
        
        print(queries, words)
        words.sort()
        output = []
        for query in queries:
            left, right = 0, len(words) - 1
            
            while left <= right:
                mid = (left + right) // 2
                
                if words[mid] > query:
                    right = mid - 1
                elif words[mid] <= query:
                    left = mid + 1
                else:
                    break
            # print("break point", left)
            output.append(len(words) - right - 1)
        return output
        