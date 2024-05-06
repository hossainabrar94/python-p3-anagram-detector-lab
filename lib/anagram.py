# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word
    
    @property
    def word(self):
        return self._word
    @word.setter
    def word(self, word):
        self._word = word

    def match(self, list):        
        matched_word = []
        for word in list:
            letters = []
            # breakpoint()
            for letter in self.word:
                # breakpoint()
                if letter in word:
                    letters.append(letter)
            joined_letter = ''.join(letters)
            if self.word == joined_letter:
                # breakpoint()
                matched_word.append(word)
        # breakpoint()
        return matched_word