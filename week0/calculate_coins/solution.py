def calculate_coins(sum):
	sum = int(sum * 100)
	coins_dict = {}
	# we need this below, because we're not sure in which order
	# will the dictionary arrange the coins
	sorted_coins = [100, 50, 20, 10, 5, 2, 1]

	for coin in sorted_coins:
		coins_dict[coin] = sum // coin
		sum -= coins_dict[coin] * coin

	return coins_dict

def main():
	print(calculate_coins(0.53))
	print(calculate_coins(8.94))

if __name__ == '__main__':
	main()