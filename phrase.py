

class Phrase:
    def __init__(self, phrase):
        #receive the phrase and assign it to the class
        self.phrase = phrase.lower()
        # self.hidden_phrase_list = []
        self.phrase_list = []
        for letter in self.phrase:
            if letter == " ":
                self.phrase_list.append(' ')
            else:
                self.phrase_list.append('_')
        self.current_phrase = "".join(self.phrase_list)
        

    def display(self):
        print(self.current_phrase)


    def check_letter(self, guess):
        guess = guess.lower()
        if guess in self.phrase:
            for idx, letter in enumerate(self.phrase):
                if guess == self.phrase[idx]:
                    self.phrase_list[idx] = guess
            self.current_phrase = "".join(self.phrase_list)
            return True
        else:
            return False

    def check_complete(self):
        return self.current_phrase == self.phrase

