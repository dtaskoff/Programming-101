from count_words import count_words

# returns the number of different words in 'arr'
def unique_words_count(arr):
	dict = count_words(arr)
	return len(dict.keys())

def main():
	print(unique_words_count(["apple", "banana", "apple", "pie"]))
	print(unique_words_count(["python", "python", "python", "ruby"]))
	print(unique_words_count(["HELLO!"] * 10))

if __name__ == '__main__':
	main()