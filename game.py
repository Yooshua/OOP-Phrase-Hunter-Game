import random
import phrase

class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = ['when in Rome',
                        'fill in the blank',
                        'where there is smoke there is fire',
                        'one for all all for one',
                        'the night is young']
        self.active_phrase = None
        self.guesses = []
        #  create a list of valid inputs
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.valid_input = []
        for letter in alphabet:
            self.valid_input.append(letter)


    def start(self):
        self.active_phrase = self.get_random_phrase()
        self.missed = 0
        current_phrase = phrase.Phrase(self.active_phrase)
        Game.welcome(self)
        # print(self.active_phrase)
        while not current_phrase.check_complete():
            current_phrase.display()
            guess = Game.get_guess(self)
            self.guesses.append(guess)
            if not current_phrase.check_letter(guess):
                self.missed += 1
                if self.missed < 5:
                    print(f'\nIncorrect!  You have used {self.missed} of 5 guesses!')
                    print(f"You have used {','.join(self.guesses)}.\n")

                else:
                    Game.game_over(self)
                    break
        print('\n\nCongratulations you won!')
        print(f'The phrase was "{self.active_phrase}"')





    def get_random_phrase(self):
        return random.choice(self.phrases)
        

    def welcome(self):
        print("=========================\nWelcome to Phrase Hunter!\n=========================")
        print("\nInstructions: try and guess a phrase by entering a letter!\n")


    def get_guess(self): #  This method gets the guess from a user and records it in the guesses attribute
        guess = ""
        while guess not in self.valid_input:
            guess = input('\nGuess a letter: ').lower()
            if guess not in self.valid_input:
                print('\nThat is not a valid input')
        return guess


    def game_over():
        print('You used all your guesses! Better luck next time!')