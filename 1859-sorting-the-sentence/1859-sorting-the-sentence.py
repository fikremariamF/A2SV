class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        word_arr = s.split()
        print(word_arr)
        new_word = []
        counter = 1
        sentence = ""
        while (len(word_arr) != 0):
            for value in word_arr:
                if int(value[-1]) == counter:
                    new_value = value[:-1]
                    new_word.append(new_value)
                    word_arr.remove(value)
                    counter = counter + 1
        for word in new_word:
            sentence = sentence + word + " "
        sentence = sentence[:-1]
        return sentence
            
            
            
        