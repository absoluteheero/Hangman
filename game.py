import random

class Game:
    bank_of_words = ["elephant", "morning", "electronic", ]

    def __init__(self, player):
        self.player = player
        self.word_to_guess = random.choice(Game.bank_of_words)
        self.number_of_tries = 5
        self.is_game_over = False
        self.guessed_letters = []
        self.guessed_word = ""

    def play_game(self):

        for c in self.word_to_guess:
            self.guessed_letters.append("*")

        self.guessed_word = "".join(self.guessed_letters)

        print("Try to guess this " + str(len(self.word_to_guess)) +" letter word " + self.player.name)
        print(self.word_to_guess)

        while self.number_of_tries != 0:

            if self.word_to_guess == self.guessed_word:
                print("Congratulations you won the game !!!")
                print("The word to guess was indeed \"" + self.word_to_guess + "\"")
                break

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
                    break

                case "3":
                    print("Goodbye !")
                    break

        if self.number_of_tries == 0:
            print("Game Over !")   

    def guess_letter(self, letter):
        number_of_correct_letters = 0
        if letter not in self.word_to_guess or letter in self.guessed_letters:
            self.number_of_tries -= 1
            return

        for index in range(0,len(self.word_to_guess)):
            if letter == self.word_to_guess[index]:
                self.guessed_letters[index] = letter
                self.guessed_word = "".join(self.guessed_letters)
            


        
    


    def guess_word(self, word):
        pass

    
