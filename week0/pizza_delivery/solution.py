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
                print(take(commands[1], float(commands[2]), order))
                saved = False
        elif cmd == "status":
            print('\n'.join(status(order)))
        elif cmd == "save":
            print(save(order))
            listed = False
            saved = True
        elif cmd == "list":
            print('\n'.join(list_()))
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
    order[name] = order.setdefault(name, price)

    return "Taking order from %s for %.2f"%(name, price)

def status(order):
    status = []

    for name in order:
        status.append(format_output(name, order[name]))

    return status

def save(order):
    ts = time()
    stamp = datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
    file_ = open('orders_%s'%stamp, "w")

    for name in order:
        file_.write(name + " - " + str(order[name]) + "\n")
    file_.close()

    return "Order saved"

def list_():
    order_files = glob("orders_????_??_??_??_??_??")

    list_ = []
    for index in range(0, len(order_files)):
        list_.append(format_output("[%d]"%(index + 1), order_files[index]))

    return list_

def load(number, order):
    order_files = glob("orders_????_??_??_??_??_??")
    file_to_load = order_files[number - 1]

    file_ = open(file_to_load, "r")
    content = file_.read()
    file_.close()

    all_orders = content.splitlines()
    all_orders = map(lambda string: string.split(" - "), all_orders)

    order = {}

    for single_order in all_orders:
        order[single_order[0]] = float(single_order[1])

    return order

def help():
     return "List of possible commands: \n"\
     + "take <name> <price>\n"\
     + "status\n"\
     + "save\n"\
     + "list\n"\
     + "load <number>\n"\
     + "finish\n"\
     + "help\n"

def unknown():
    return "Unknown command.\n"\
        + "Try entering help for further information."

def format_output(fst, snd):
    if type(snd) == type(0.00):
        return "%s - %.2f"%(fst, snd)
    else:
        return "%s - %s"%(fst, snd)

def main():
    pizza_delivery()

if __name__ == '__main__':
    main()