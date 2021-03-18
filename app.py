import game


# Create your Dunder Main statement.
if __name__ == '__main__':
    game = game.Game()
    while True:
        game.start()
        play_again = input('\nWould you like to play again? (y/n) ')
        if not play_again.lower() == 'y':
            break
    print('Thanks for playing!')
