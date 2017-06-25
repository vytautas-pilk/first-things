# A very simple implementation of 'Guess the number' game.

import random

secret_number = random.randrange(0, 100)

attempts = 7
version = 1
active = True

print("Enter 'q' to exit.")

while active:
	a_guess = input("Your guess: ")

	if a_guess == 'q':
		active = False
	elif int(a_guess) < secret_number:
		attempts -= 1
		print("Higher! You have " + str(attempts) + " attempts left.\n")
		if attempts == 0:
			print("Game over. The number was " + str(secret_number) + "\n\n")
			attempts = 7
			secret_number = random.randrange(0, 100)
	elif int(a_guess) > secret_number:
		attempts -= 1
		print("Lower! You have " + str(attempts) + " attempts left.\n")
		if attempts == 0:
			print("Game over. The number was " + str(secret_number) + "\n\n")
			attempts = 7
			secret_number = random.randrange(0, 100)
	elif int(a_guess) == secret_number:
		print("Success!\n\nNew game!\nEnter 'q' to quit")
		attempts = 7
		secret_number = random.randrange(0, 100)
