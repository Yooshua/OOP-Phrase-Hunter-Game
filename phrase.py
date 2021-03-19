

class Phrase:
    def __init__(self, phrase):
        #receive the phrase and assign it to the class
        self.phrase = phrase.lower()
        self.winning_phrase_list = []
        self.phrase_list = []
        self.winning_phrase = ""
        self.current_phrase = ""


    def display(self):
        print(self.current_phrase)


    def check_letter(self, guess):
        guess = guess.lower()
        if guess in self.phrase:
            for idx, letter in enumerate(self.phrase):
                if guess == self.phrase[idx]:
                    self.phrase_list[idx] = guess
            self.current_phrase = " ".join(self.phrase_list)
            return True
        else:
            return False

    def check_complete(self):
        return self.current_phrase == self.winning_phrase

    def reset_phrase(self):
        self.winning_phrase_list = []
        self.phrase_list = []
        for letter in self.phrase:
            if letter == " ":
                self.winning_phrase_list.append(letter)
                self.phrase_list.append(' ')
            else:
                self.winning_phrase_list.append(letter)
                self.phrase_list.append('_')
        self.winning_phrase = " ".join(self.winning_phrase_list)
        self.current_phrase = " ".join(self.phrase_list)