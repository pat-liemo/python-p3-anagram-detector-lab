# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word
        
    def match(self, word_list):
        self.word_list = word_list
        matched_list = []
        
        target = [letter for letter in self.word]
        
        for new_word in word_list:
            letter_list = [letter for letter in new_word]
            if sorted(target) == sorted(letter_list):
                matched_list.append(new_word)
            else:
                None
                
        return matched_list    