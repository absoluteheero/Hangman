from player import Player
from game import Game

print("Hi, and welcome to hangman !")

player_name = input("What is your name ?")

print("\n")

player_1 = Player(player_name)

game = Game(player_1)
game.play_game()