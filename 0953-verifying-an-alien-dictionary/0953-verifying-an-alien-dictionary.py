class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphabetdict = {}
        for i in range(len(order)):
            alphabetdict[order[i]] = i + 1
        for i in range(len(words)-1):
            word = words[i]
            nextWord= words[i+1]
            for l in range(len(word)):
                # print(word[l],":",alphabetdict[word[l]],"-",nextWord[l],":",alphabetdict[nextWord[l]] )
                if l < len(nextWord) and alphabetdict[word[l]] < alphabetdict[nextWord[l]]:
                    break
                elif l >= len(nextWord) or alphabetdict[word[l]] > alphabetdict[nextWord[l]]:
                    return False
        return True
            
        