import random
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
import urllib.request



colorama_init()

class Game:

    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
    response = urllib.request.urlopen(word_site)
    long_txt = response.read().decode()
    words = long_txt.splitlines()

    def __init__(self, player):
        self.player = player
        self.word_to_guess = ""
        self.number_of_tries = 5
        self.guessed_letters = []
        self.guessed_word = ""

    def play_game(self):

        self.initialize_game()

        for c in self.word_to_guess:
            self.guessed_letters.append("*")

        self.guessed_word = "".join(self.guessed_letters)

        print("Try to guess this " + str(len(self.word_to_guess)) +" letter word " + self.player.name)

        while self.number_of_tries != 0:

            if self.word_to_guess == self.guessed_word:
                print("Congratulations you won the game !!!")
                print("The word to guess was indeed " + Fore.GREEN + self.word_to_guess + Style.RESET_ALL)


                self.play_again()       

            print(self.guessed_word)
            print("You have " + Fore.RED + str(self.number_of_tries) + Style.RESET_ALL + " chances left.")
            print(Fore.GREEN + "Choices" + Style.RESET_ALL)
            print(Fore.YELLOW + "1. Guess a letter")
            print("2. Guess the word")
            print("3. Quit the game" + Style.RESET_ALL)
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
            print(Fore.RED + "Game Over !" + Style.RESET_ALL + " The word was " + Fore.RED + self.word_to_guess + Style.RESET_ALL)
            self.play_again()
                    

    def initialize_game(self):
        self.word_to_guess = random.choice(Game.words)
        print(self.word_to_guess)
        self.number_of_tries = 5
        self.guessed_letters = []
        self.guessed_word = ""


    def guess_letter(self, letter):
        number_of_correct_letters = 0
        if letter not in self.word_to_guess or letter in self.guessed_letters:
            self.number_of_tries -= 1
            return

        for index in range(0,len(self.word_to_guess)):
            if letter == self.word_to_guess[index]:
                self.guessed_letters[index] = letter
                self.guessed_word = "".join(self.guessed_letters)
                number_of_correct_letters += 1
 
        print("There is " + str(number_of_correct_letters) + " \"" + letter + "\"")


    def guess_word(self, word):
        if word == self.word_to_guess:
            self.guessed_word = word
            return
            
        else:
            self.number_of_tries -= 1

    def play_again(self):
        print("Want to play again ?")
        print(Fore.GREEN + "Choices:" + Style.RESET_ALL)
        print("1. Yes")
        print("2. No")
        choice = input("What do you do?")

        match choice:
            case "1":
                self.play_game()

            case "2":
                print(Fore.YELLOW + "Goodbye !" + Style.RESET_ALL)
                exit()

            

    
