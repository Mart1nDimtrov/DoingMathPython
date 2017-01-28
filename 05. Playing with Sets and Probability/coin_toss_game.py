'''
#3: How Many Tosses Before You Run Out of Money?
Let’s consider a simple game played with a fair coin toss. A player wins 
$1 for heads and loses $1.50 for tails. The game is over when the player’s 
balance reaches $0. Given a certain starting amount specified by the user 
as input, your challenge is to write a program that simulates this game. 
Assume there’s an unlimited cash reserve with the computer—your opponent here.
'''
import random

def toss():
	# 0 -> Heads, 1-> Tails
	if random.random() < 1/2:
		return 0
	else:
		return 1

def play_game(amount):
	tosses = 0
	while amount > 0:
		tosses = tosses + 1
		coin_toss = toss()
		if (coin_toss == 1):
			amount -= 1.5
			print("Tails! Current amount: {0}".format(amount))
		else:
			amount += 1
			print("Heads! Current amount: {0}".format(amount))
	print("Game over :( Current amount {0:.2f}. Coin tosses: {1}".format(amount, tosses))


amount = int(input("Enter your starting amount: "))
play_game(amount)
