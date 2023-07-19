import random

class Game:
    bank_of_words = ["elephant", "morning", "electronic", "important" , "technology",
                      "programming", "insurance", "ability", "paperback", "calculator",
                        "computer", "ordinary", "football", "policeman", "monitor", "surgery",
                         "foreigner", "transmission", "dictionary", "skating", "boulevard" ]

    def __init__(self, player):
        self.player = player
        self.word_to_guess = random.choice(Game.bank_of_words)
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
                print("The word to guess was indeed \"" + self.word_to_guess + "\"")


                self.play_again()       

            print(self.guessed_word)
            print("You have " + str(self.number_of_tries) + " chances left.")
            print("Choices:")
            print("1. Guess a letter")
            print("2. Guess the word")
            print("3. Quit the game")
            choice = input("What do you want to do ?")
            
            match choice:
                case "1":
                    letter = input("What is your letter guess ?")
                    self.guess_letter(letter)
                    

                case "2":
                    word = input("What is your word guess ?")
                    self.guess_word(word)

                case "3":
                    print("Goodbye !")
                    break

        if self.number_of_tries == 0:
            print("Game Over !")
            self.play_again()
                    

    def initialize_game(self):
        self.word_to_guess = random.choice(Game.bank_of_words)
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
        print("Choices:")
        print("1. Yes")
        print("2. No")
        choice = input("What do you do?")

        match choice:
            case "1":
                self.play_game()

            case "2":
                print("Goodbye !")
                exit()

            

    
