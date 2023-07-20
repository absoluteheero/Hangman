import random
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
import urllib.request
from os import system, name



colorama_init()

class Game:

    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
    response = urllib.request.urlopen(word_site)
    long_txt = response.read().decode()
    words = long_txt.splitlines()
    filtered_words = []
    
    for word in words:
        if len(word) > 6:
            filtered_words.append(word)
            

    def __init__(self, player):
        self.player = player
        self.word_to_guess = ""
        self.number_of_tries = 5
        self.guessed_letters = []
        self.guessed_word = ""
        self.guesses = []

    def play_game(self):

        self.show_logo()

        self.initialize_game()

        for c in self.word_to_guess:
            self.guessed_letters.append("*")

        self.guessed_word = "".join(self.guessed_letters)

        print("\n")
        print(self.player.name + ", try to guess this " + str(len(self.word_to_guess)) +" letter word ")
        print("\n")

        while self.number_of_tries != 0:

            if self.word_to_guess == self.guessed_word:
                print("\n")
                print("Congratulations you won the game !!!")
                print("The word to guess was indeed " + Fore.GREEN + self.word_to_guess.upper() + Style.RESET_ALL)


                self.play_again()


            print(self.guessed_word)
            print("\n")
            print("You have " + Fore.RED + str(self.number_of_tries) + Style.RESET_ALL + " chances left.")
            print("Letters already taken:")
            print(self.guesses)
            print(Fore.GREEN + "Choices" + Style.RESET_ALL)
            print(Fore.YELLOW + "1. Guess a letter")
            print("2. Guess the word")
            print("3. Quit the game" + Style.RESET_ALL)
            print("\n")
            choice = input("What do you want to do ?")
            
            match choice:
                case "1":
                    letter = input("What is your letter guess ?")
                    self.guess_letter(letter)
                    

                case "2":
                    word = input("What is your word guess ?")
                    self.guess_word(word)

                case "3":
                    print(Fore.YELLOW + "Goodbye !" + Style.RESET_ALL)
                    exit()

        if self.number_of_tries == 0:
            print(Fore.RED + "Game Over !" + Style.RESET_ALL + " The word was " + Fore.RED + self.word_to_guess.upper() + Style.RESET_ALL)
            self.play_again()
                    

    def initialize_game(self):
        self.word_to_guess = random.choice(Game.filtered_words)
        self.number_of_tries = 5
        self.guessed_letters = []
        self.guessed_word = ""
        self.guesses =[]


    def guess_letter(self, letter):
        self.clear()
        self.show_logo()
        guess = letter.lower()
        number_of_correct_letters = 0
        if guess not in self.guesses:
            self.guesses.append(guess)
            
        if guess not in self.word_to_guess or guess in self.guessed_letters:
            self.number_of_tries -= 1
            print("There is no " + Fore.RED + guess.upper() + Style.RESET_ALL)
            return

        for index in range(0,len(self.word_to_guess)):
            if guess == self.word_to_guess[index]:
                self.guessed_letters[index] = guess
                self.guessed_word = "".join(self.guessed_letters)
                number_of_correct_letters += 1
 
        print("There is " + str(number_of_correct_letters) + " " + Fore.GREEN + guess.upper() + Style.RESET_ALL)


    def guess_word(self, word):
        if word == self.word_to_guess:
            self.guessed_word = word
            return
            
        else:
            self.number_of_tries -= 1

    def play_again(self):
        print("\n")
        print("Want to play again ?")
        print(Fore.GREEN + "Choices:" + Style.RESET_ALL)
        print("1. Yes")
        print("2. No")
        choice = input("What do you do?")

        match choice:
            case "1":
                self.clear()
                self.play_game()

            case "2":
                print(Fore.YELLOW + "Goodbye !" + Style.RESET_ALL)
                exit()

    def clear(self):
        # for windows
        if name == 'nt':
            _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')


    def show_logo(self):
        logo = """
 .----------------.  .----------------.  .-----------------. .----------------.  .----------------.  .----------------.  .-----------------.
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |  ____  ____  | || |      __      | || | ____  _____  | || |    ______    | || | ____    ____ | || |      __      | || | ____  _____  | |
| | |_   ||   _| | || |     /  \     | || ||_   \|_   _| | || |  .' ___  |   | || ||_   \  /   _|| || |     /  \     | || ||_   \|_   _| | |
| |   | |__| |   | || |    / /\ \    | || |  |   \ | |   | || | / .'   \_|   | || |  |   \/   |  | || |    / /\ \    | || |  |   \ | |   | |
| |   |  __  |   | || |   / ____ \   | || |  | |\ \| |   | || | | |    ____  | || |  | |\  /| |  | || |   / ____ \   | || |  | |\ \| |   | |
| |  _| |  | |_  | || | _/ /    \ \_ | || | _| |_\   |_  | || | \ `.___]  _| | || | _| |_\/_| |_ | || | _/ /    \ \_ | || | _| |_\   |_  | |
| | |____||____| | || ||____|  |____|| || ||_____|\____| | || |  `._____.'   | || ||_____||_____|| || ||____|  |____|| || ||_____|\____| | |
| |              | || |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
"""
        print(logo)

    
