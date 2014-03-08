# script that solves Problem F7 from week0/simple_problems3
from time import time
from glob import glob
from datetime import datetime

def pizza_delivery():
	order = {}
	listed = False
	saved = True

	while True:
		command = input("Enter command: ")
		commands = command.split()
		cmd = commands[0]

		if cmd == "take":
			if len(commands) < 3:
				unknown()
			else:
				take(commands[1], float(commands[2]), order)
				saved = False
		elif cmd == "status":
			status(order)
		elif cmd == "save":
			save(order)
			listed = False
			saved = True
		elif cmd == "list":
			list()
			listed = True
		elif cmd == "load":
			if listed and saved:
				order = load(int(commands[1]), order)
				listed = False
			elif not saved:
				print("You have not saved the current order.")
				print("If you wish to discard it, type load <number> again.")
				saved = True
			else:
				print("Use list command before loading")
		elif cmd == "finish":
			if not saved:
				print("You have not saved your order.")
				print("If you wish to continue, type finish again.")
				print("If you want to save your order, type save")
				saved = True
			else:
				print("Finishing order. Bye!")
				break
		elif cmd == "help":
			help()
		else:
			unknown()

def take(name, price, order):
	if name in order:
		order[name] += price
	else:
		order[name] = price
	print("Taking order from %s for %.2f"%(name, price))

def status(order):
	for name in order:
		format_output(name, order[name])

def save(order):
	ts = time()
	stamp = datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
	file = open('orders_%s'%stamp, "w")

	for name in order:
		file.write(name + " - " + str(order[name]) + "\n")
	file.close()

	print("Order saved")

def list():
	order_files = glob("orders_????_??_??_??_??_??")

	for index in range(0, len(order_files)):
		format_output("[%d]"%(index + 1), order_files[index])

def load(number, order):
	order_files = glob("orders_????_??_??_??_??_??")
	file_to_load = order_files[number - 1]

	file = open(file_to_load, "r")
	content = file.read()
	file.close()

	all_orders = content.splitlines()
	all_orders = map(lambda string: string.split(" - "), all_orders)

	order = {}

	for single_order in all_orders:
		order[single_order[0]] = float(single_order[1])

	return order

def help():
	print("List of possible commands: ")
	print("take <name> <price>")
	print("status")
	print("save")
	print("list")
	print("load <number>")
	print("finish")
	print("help")

def unknown():
	print("Unknown command.")
	print("Try entering help for further information.")

def format_output(fst, snd):
	if type(snd) == type(0.00):
		print("%s - %.2f"%(fst, snd))
	else:
		print("%s - %s"%(fst, snd))

def main():
	pizza_delivery()

if __name__ == '__main__':
	main()