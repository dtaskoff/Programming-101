# returns all occurrences of 'needle' in 'haystack'
def count_substrings(haystack, needle):
	count = 0
	needle_size = len(needle)
	haystack_size = len(haystack)

	i = 0
	while i < haystack_size:
		if haystack[i : (i + needle_size)] == needle:
			count += 1
			i += needle_size
		else:
			i += 1

	return count

def main():
	print(count_substrings("This is a test string", "is"))
	print(count_substrings("babababa", "baba"))
	print(count_substrings("Python is an awesome language to program in!", "o"))
	print(count_substrings("We have nothing in common!", "really?"))
	print(count_substrings("This is this and that is this", "this"))


if __name__ == '__main__':
	main()