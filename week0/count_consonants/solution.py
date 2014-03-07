# returns the number of consonants in 'str'
def count_consonants(str):
	consonants = "bcdfghjklmnpqrstvwxz"
	count = 0

	for char in str:
		if char.lower() in consonants:
			count += 1

	return count
#	short way:
#	len([char for char in str if char.lower() in consonants])

def main():
	print(count_consonants("Python"))
	print(count_consonants("Theistareykjarbunga")) #It's a volcano name!
	print(count_consonants("grrrrgh!"))
	print(count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"))
	print(count_consonants("A nice day to code!"))


if __name__ == '__main__':
	main()