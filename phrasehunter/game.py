class Game:
    def __init__(self):
        self.missed = 0
        #  used to track the number of incorrect guesses by the user.
        #  The initial value is 0 since no guesses have been made at the start of the game.

        self.phrases = ['list of the phrases!']
        #  a list of five Phrase objects to use with the game. A phrase should 
        #  only include letters and spaces -- no numbers, puntuation or other special characters.

        self.active_phrase = None
        #  This is the Phrase object that's currently in play. The initial value will be None. 
        #  Within the start_game() method, this property will be set to the Phrase object 
        #  returned from a call to the get_random_phrase() method.
        
        self.guesses = 0

    def start(self):
        #  Calls the welcome method, creates the game loop, calls the get_guess method,
        #  adds the user's guess to guesses, increments the number of missed by one if the
        #  guess is incorrect, calls the game_over method.

    def get_random_phrase(self):
        #  this method randomly retrieves one of the phrases stored in the phrases list and returns it.

    def welcome(self): #  Welcomes a player at the start of the game.

    def get_guess(self): #  This method gets the guess from a user and records it in the guesses attribute