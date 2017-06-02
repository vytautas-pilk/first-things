import random

# A simple program to generate a thirteen-symbol password which should
# be permitted on most websites.

def password_generator():
	"""A function which returns a newly generated password using symbols
	from the list."""
	symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
	'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
	'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 
	'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', 
	'2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '$', '%', '^', '&', 
	'_', '-']
	password = ''
	while len(password) != 13:
		password = password + random.choice(symbols)
	
	return password
