# the string_utils module solving
# problems 1 and 2

# takes a string and returns a list
# formed from all lines
def lines(text):
	return text.splitlines()

# takes a list from strings and
# returns them joined by a newlines
def unlines(elements):
	return "\n".join(elements); 

# these two are analogue to these
# above, but join and split by spaces
def words(text):
	return text.split()

def unwords(elements):
	return " ".join(elements)

# takes a string and a number and replaces
# all tabs in it with that number of spaces
def tabs_to_spaces(str, one_tab_n_spaces = 4):
	return str.replace('\t', ' ' * one_tab_n_spaces)