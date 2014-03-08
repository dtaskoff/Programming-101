# returns True if 'word' is in "a"^n"b"^n form (n > 0)
def is_an_bn(word):
	ays_and_bees = word.split('ab')
	bees_and_ays = word.split('ba')
	return len(ays_and_bees) == 2 and len(bees_and_ays) == 1 and \
		len(ays_and_bees[0]) == len(ays_and_bees[1])

def main():
	print(is_an_bn(""))
	print(is_an_bn("rado"))
	print(is_an_bn("aaabb"))
	print(is_an_bn("aaabbb"))
	print(is_an_bn("aabbaabb"))
	print(is_an_bn("bbbaaa"))
	print(is_an_bn("aaaaabbbbb"))
	print(is_an_bn("baba"))

if __name__ == '__main__':
	main()