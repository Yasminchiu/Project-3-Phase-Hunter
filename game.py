from phrase import Phrase
import random
import string


class Game:
    
    
    def __init__(self):
        
        self.missed = 0
        self.phrases = [
            Phrase("live long and prosper"), 
            Phrase("diamonds are forever"), 
            Phrase("an apple a day keeps the doctor away"), 
            Phrase("walking on sunshine"), 
            Phrase("the early bird gets the worm")
        ]
        self.active_phrase = random.choice(self.phrases)
        self.guesses = []
        self.name = ""
        self.games_played = 0
        
        
    def welcome(self):
        
        print("=" * 24, "\n\033[1mWelcome to PHASE HUNTER!\033[0m")
        print("=" * 24)
        self.name = input("\nWhat should I call you?: ")
        print(f"\n{self.name}, do you think you guess the phrase in \033[1m5\033[0m or less tries?\n...Let's find out!\n")
        print(f"\033[1mIncorrect guesses:\033[0m {self.missed} \n")
        
        
    def get_guess(self):
        
        self.guess = input("\n\nEnter a letter: ").lower()
        return self.guess
    
    
    def game_over(self):
        
        if self.missed == 5:
            print("Sorry but you're out of guesses! Better luck next time!\n")
            print("*" * 10, "\033[1m GAME OVER \033[0m", "*" * 10)
        else:
            print("*" * 10, f"\033[1mCONGRATS! YOU'RE A WINNER!\033[0m", "*" * 10)
            
        play_again = input(f"\nWould you like to play again {self.name}? (Enter yes/no): ").lower()
        if play_again == "yes":
            Game.reset_game(self)
            Game.start(self)
        elif play_again == "no":
            print(f"\nThanks for playing {self.name}. See you next time!")
    
        
    def start(self):
        
        if self.games_played == 0:
            Game.welcome(self)
        
        while(self.missed < 5 and self.active_phrase.check_complete(self.guesses) == False):
        
            Phrase.display(self.active_phrase, self.guesses)
            
            user_guess = self.get_guess()
            self.guesses.append(user_guess)
            
            alphabet = list(string.ascii_lowercase)
            if self.guess not in alphabet:
                print("(That's not a valid letter! Please try again)")
            
            if self.active_phrase.check_guess(user_guess):
                print("\nNice! You guessed a letter in the phrase!\n")
            else:
                print("\nOops! That's not a letter in the phrase...\n")
                self.missed += 1
                print(f"\033[1mIncorrect guesses:\033[0m {self.missed} \n")
        
        Game.game_over(self)
        
    
    def reset_game(self):
        
        self.missed = 0
        self.active_phrase = random.choice(self.phrases)
        self.guesses = []
        self.name = self.name
        self.games_played += 1
               