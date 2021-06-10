# import pandas as pd
# import json
# from argparse import ArgumentParser
import sys

# reg_num_and_color[color].append(reg_num)
reg_num_and_color = dict()
# reg_num_and_slot_num[reg_num] = slot_num
reg_num_and_slot_num = dict()
# color_and_slot_num[color].append(slot_num)
color_and_slot_num = dict()
size_of_the_parking = 0
occupancy_array = list()


class Car:
    def __init__(self, color, reg_num):
        self.color = color
        self.reg_num = reg_num


def find_status():
    global occupancy_array
    # print("{0}    {1}    {2} ".format("Slot No.", "Registration No", "Colour"))
    print("Slot No.    Registration No    Colour")
    # print("{0}{1}{2}{3}{4} ".format("Slot No.", "\t", "Registration No", "\t", "Colour"))
    for i in range(len(occupancy_array)):
        if occupancy_array[i]:
            print("{0}           {1}      {2}".format(str(i+1), occupancy_array[i].reg_num, occupancy_array[i].color))


# $ status
# Slot No.
# 1
# 2
# 3
# 5
# 6
# Registration No
# KA-01-HH-1234
# KA-01-HH-9999
# KA-01-BB-0001
# KA-01-HH-2701
# KA-01-HH-3141
# Colour
# White
# White
# Black
# Blue
# Black


# $ create_parking_lot 6
# Created a parking lot with 6 slots
def create_parking_lot(n):
    # print("creating parking lot")
    global size_of_the_parking
    size_of_the_parking = n
    global occupancy_array
    occupancy_array = [None for _ in range(n)]
    # print("occupancy_array : {0}".format(occupancy_array))
    return "Created a parking lot with {0} slots".format(int(n))


# $ leave 4
# Slot number 4 is free
def is_vehicle_present(slot_number):
    global occupancy_array
    if occupancy_array[slot_number]:
        return True
    else:
        return False


def leave_the_vehicle(slot_number):
    if is_vehicle_present(slot_number):
        global occupancy_array
        # occupancy_array.pop(slot_number)
        # occupancy_array.insert(slot_number, None)
        occupancy_array[slot_number-1] = None
        return "Slot number {0} is free".format(slot_number)
    else:
        return "Sorry, slot_number:{0} is already occupied".format(slot_number)


# $ park KA-01-P-333 White
# Allocated slot number: 4
# $ park DL-12-AA-9999 White
# Sorry, parking lot is full
def is_parking_full():
    global occupancy_array
    # print("inside is_parking_full : occupancy_array :{0}".format(occupancy_array))
    for i in range(len(occupancy_array)):
        if occupancy_array[i] is None:
            # print("not full")
            return False
    else:
        # print("parking is FULL")
        return True


def find_nearest_slot_avl():
    global occupancy_array
    for i in range(len(occupancy_array)):
        if occupancy_array[i] is None:
            slot_num = i+1
            return slot_num


def park(reg_num, color):
    if is_parking_full():
        return "Sorry, parking lot is full"
    else:
        c1 = Car(color, reg_num)
        slot_num = int(find_nearest_slot_avl())
        reg_num_list = [reg_num]
        slot_num_list = [slot_num]
        try:
            reg_num_and_color[color].append(reg_num)
        except KeyError:
            reg_num_and_color[color] = reg_num_list
        except ValueError as err_msg:
            raise ValueError("problem in find_slot_numbers_for_cars_with_colour : {0}".format(str(err_msg)))

        try:
            reg_num_and_slot_num[reg_num] = slot_num
        except KeyError:
            print("reg number is unique so if a car with the particular reg num is"
                  " already parked it cant be parked again untill or unless its gone out")
        except ValueError as err_msg:
            raise ValueError("problem in find_slot_numbers_for_cars_with_colour : {0}".format(str(err_msg)))

        try:
            color_and_slot_num[color].append(slot_num)
        except KeyError:
            color_and_slot_num[color] = slot_num_list
        except ValueError as err_msg:
            raise ValueError("problem in find_slot_numbers_for_cars_with_colour : {0}".format(str(err_msg)))

        slot_number = find_nearest_slot_avl()
        occupancy_array[slot_number - 1] = c1
        return "Allocated slot number: {0}".format(slot_num)


#  $ registration_numbers_for_cars_with_colour White
# KA-01-HH-1234, KA-01-HH-9999, KA-01-P-333
def find_registration_numbers_for_cars_with_colour(color):
    # reg_num_and_color = json.dump(reg_num_and_color.json)
    try:
        list_of_reg_num = reg_num_and_color[color]
        return list_of_reg_num
    except KeyError:
        return "Not found"
    except ValueError as err_msg:
        raise ValueError("problem in find_slot_numbers_for_cars_with_colour : {0}".format(str(err_msg)))


# $ slot_numbers_for_cars_with_colour White
# 1, 2, 4
# $ slot_number_for_registration_number KA-01-HH-3141
# 6
# $ slot_number_for_registration_number MH-04-AY-1111
# Not found
def find_slot_numbers_for_cars_with_colour(color):
    global color_and_slot_num
    # reg_num_and_color = json.dump(reg_num_and_color.json)
    try:
        list_of_reg_num = color_and_slot_num[color]
        return list_of_reg_num
    # except KeyError:
    #     return "Not found"
    except ValueError as err_msg:
        raise ValueError("problem in find_slot_numbers_for_cars_with_colour : {0}".format(str(err_msg)))


def find_slot_number_for_registration_number(reg_num):
    global color_and_slot_num
    try:
        slot_num = reg_num_and_slot_num[reg_num]
        return slot_num
    except KeyError:
        return "Not found"
    except ValueError as err_msg:
        raise ValueError("problem in find_slot_number_for_registration_number: {0}".format(str(err_msg)))


def display_formating_for_list(response):
    # print("response : {0}".format(response))
    str_sol = ""
    for item in response[:-1]:
        str_sol += str(item) + ", "
    str_sol += str(response[-1])
    print(str_sol)


def run_as_interactive_input():
    while 1:
        cmd_str = input()
        if cmd_str == "exit":
            return

        else:
            cmd_list = cmd_str.split()
            if len(cmd_list) == 1 and cmd_list[0] == "status":
                find_status()

            elif len(cmd_list) == 2:
                if cmd_list[0] == "create_parking_lot":
                    response = create_parking_lot(int(cmd_list[1]))
                    print(response)
                elif cmd_list[0] == "leave":
                    response = leave_the_vehicle(slot_number=int(cmd_list[1]))
                    print(response)
                elif cmd_list[0] == "registration_numbers_for_cars_with_colour":
                    response = find_registration_numbers_for_cars_with_colour(color=cmd_list[1])
                    display_formating_for_list(response)
                elif cmd_list[0] == "slot_numbers_for_cars_with_colour":
                    response = find_slot_numbers_for_cars_with_colour(color=cmd_list[1])
                    display_formating_for_list(response)
                elif cmd_list[0] == "slot_number_for_registration_number":
                    response = find_slot_number_for_registration_number(reg_num=cmd_list[1])
                    print(response)

            elif len(cmd_list) == 3:
                if cmd_list[0] == "park":
                    response = park(reg_num=cmd_list[1], color=cmd_list[2])
                    print(response)

            else:
                print("Enter correct command")


def run_as_per_file_input(file_name):
    with open(file_name, "r") as f1:
        data = f1.readlines()

    for cmd_str in data:
        if cmd_str == "exit":
            return

        else:
            cmd_list = cmd_str.split()
            if len(cmd_list) == 1 and cmd_list[0] == "status":
                find_status()

            elif len(cmd_list) == 2:
                if cmd_list[0] == "create_parking_lot":
                    response = create_parking_lot(int(cmd_list[1]))
                    print(response)
                elif cmd_list[0] == "leave":
                    response = leave_the_vehicle(slot_number=int(cmd_list[1]))
                    print(response)
                elif cmd_list[0] == "registration_numbers_for_cars_with_colour":
                    response = find_registration_numbers_for_cars_with_colour(color=cmd_list[1])
                    display_formating_for_list(response)
                elif cmd_list[0] == "slot_numbers_for_cars_with_colour":
                    response = find_slot_numbers_for_cars_with_colour(color=cmd_list[1])
                    display_formating_for_list(response)
                elif cmd_list[0] == "slot_number_for_registration_number":
                    response = find_slot_number_for_registration_number(reg_num=cmd_list[1])
                    print(response)

            elif len(cmd_list) == 3:
                if cmd_list[0] == "park":
                    response = park(reg_num=cmd_list[1], color=cmd_list[2])
                    print(response)

            else:
                print("Enter correct command")


def main():
    # print(len(sys.argv))

    if len(sys.argv) > 1:
        # input is from file
        run_as_per_file_input(sys.argv[1])
    else:
        run_as_interactive_input()


if __name__ == '__main__':
    main()
