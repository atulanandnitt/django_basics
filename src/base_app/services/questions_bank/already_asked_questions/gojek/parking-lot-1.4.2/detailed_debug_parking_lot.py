# import pandas as pd
# import json
# from argparse import ArgumentParser
import sys

# data_object_1[color].append(reg_num)
data_object_1 = dict()
# data_object_2[reg_num] = slot_num
data_object_2 = dict()
# data_object_3[color].append(slot_num)
data_object_3 = dict()
size_of_the_parking = 0
occupancy_array = list()


class Car:
    def __init__(self, color, reg_num):
        self.color = color
        self.reg_num = reg_num


def find_status():
    global occupancy_array
    print("{0}    {1}    {2} ".format("Slot No.", "Registration No", "Colour"))
    for i in range(len(occupancy_array)):
        if occupancy_array[i]:
            print("{0}           {1}      {2}".format(i+1, occupancy_array[i].reg_num, occupancy_array[i].color))


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
    return "Created a parking lot with {0} slots".format(n)


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
    # print("parking vehicle number :{0} of color:{1}".format(reg_num, color))
    if is_parking_full():
        return "Sorry, parking lot is full"
    else:
        c1 = Car(color, reg_num)
        # slot_num = str(find_nearest_slot_avl())
        slot_num = int(find_nearest_slot_avl())
        # data_object_1[color].append(c1.reg_num)
        reg_num_list = [reg_num]
        slot_num_list = [slot_num]
        try:
            data_object_1[color].append(reg_num)
        except KeyError:
            # print("1st car got parked of color: {0}".format(color))
            data_object_1[color] = reg_num_list

        try:
            data_object_2[reg_num] = slot_num
            # print("car reg_num : {0} got parked at slot num: {1}".format(reg_num, slot_num))
        except KeyError:
            print("reg number is unique so if a car with the particular reg num is"
                  " already parked it cant be parked again untill or unless its gone out")

        try:
            data_object_3[color].append(slot_num)
        except KeyError:
            data_object_3[color] = slot_num_list

        slot_number = find_nearest_slot_avl()
        # occupancy_array.insert(slot_number-1, c1)
        occupancy_array[slot_number - 1] = c1
        return "Allocated slot number: {0}".format(slot_num)


#  $ registration_numbers_for_cars_with_colour White
# KA-01-HH-1234, KA-01-HH-9999, KA-01-P-333
def find_registration_numbers_for_cars_with_colour(color):
    # data_object_1 = json.dump(data_object_1.json)
    try:
        list_of_reg_num = data_object_1[color]
        return list_of_reg_num
    except KeyError:
        return "Not found"
    except Exception as err_msg:
        return err_msg


# $ slot_numbers_for_cars_with_colour White
# 1, 2, 4
# $ slot_number_for_registration_number KA-01-HH-3141
# 6
# $ slot_number_for_registration_number MH-04-AY-1111
# Not found
def find_slot_numbers_for_cars_with_colour(color):
    global data_object_3
    # data_object_1 = json.dump(data_object_1.json)
    try:
        list_of_reg_num = data_object_3[color]
        return list_of_reg_num
    # except KeyError:
    #     return "Not found"
    except ValueError as err_msg:
        raise ValueError("problem : {0}".format(str(err_msg)))


def find_slot_number_for_registration_number(reg_num):
    global data_object_3
    try:
        slot_num = data_object_2[reg_num]
        return slot_num
    except KeyError:
        return "Not found"
    except ValueError as err_msg:
        raise ValueError("problem in find_slot_number_for_registration_number: {0}".format(str(err_msg)))


def display_formating_for_list(response):
    # print("response :{0} and type(response) : {1}".format(response, type(response)))
    for item in response[:-1]:
        str_sol = str(item) + ", "
    str_sol += str(response[-1])
    print(str_sol)


def run_as_interactive_input():
    while 1:
        cmd_str = input()
        # print("ur input is :{0}".format(cmd_str))

        if cmd_str == "exit":
            # print("ur input is :{0}".format(cmd_str))
            return

        else:
            # cmd = input().split()
            cmd_list = cmd_str.split()
            # print("ur input is :{0}".format(cmd_str))
            if len(cmd_list) == 1 and cmd_list[0] == "status":
                # print("ur input is :{0}".format(cmd_str))
                find_status()

            elif len(cmd_list) == 2:
                if cmd_list[0] == "create_parking_lot":
                    # print("ur input is :{0}".format(cmd_str))
                    response = create_parking_lot(int(cmd_list[1]))
                    print(response)
                elif cmd_list[0] == "leave":
                    # print("ur input is :{0}".format(cmd_str))
                    response = leave_the_vehicle(slot_number=int(cmd_list[1]))
                    print(response)
                elif cmd_list[0] == "registration_numbers_for_cars_with_colour":
                    # print("ur input is :{0}".format(cmd_list))
                    response = find_registration_numbers_for_cars_with_colour(color=cmd_list[1])
                    display_formating_for_list(response)
                elif cmd_list[0] == "slot_numbers_for_cars_with_colour":
                    # print("ur input is :{0}".format(cmd_str))
                    response = find_slot_numbers_for_cars_with_colour(color=cmd_list[1])
                    display_formating_for_list(response)
                elif cmd_list[0] == "slot_number_for_registration_number":
                    # print("ur input is :{0}".format(cmd_str))
                    response = find_slot_number_for_registration_number(reg_num=cmd_list[1])
                    print(response)

            elif len(cmd_list) == 3:
                if cmd_list[0] == "park":
                    # print("ur input is :{0}".format(cmd_str))
                    # print("ur input is :{0}, {1}, {2}".format(cmd_list[0], cmd_list[1], cmd_list[2]))
                    response = park(reg_num=cmd_list[1], color=cmd_list[2])
                    print(response)
                    # park(reg_num, color)
                    # park KA-01-P-333 White

            else:
                print("Enter correct command")


def run_as_per_file_input(file_name):
    with open(file_name, "r") as f1:
        data = f1.readlines()

    for cmd_str in data:
        # # print("ur input is :{0}".format(cmd_str))

        if cmd_str == "exit":
            # # print("ur input is :{0}".format(cmd_str))
            return

        else:
            # cmd = input().split()
            cmd_list = cmd_str.split()
            # # print("ur input is :{0}".format(cmd_str))
            if len(cmd_list) == 1 and cmd_list[0] == "status":
                # # print("ur input is :{0}".format(cmd_str))
                find_status()

            elif len(cmd_list) == 2:
                if cmd_list[0] == "create_parking_lot":
                    # print("ur input is :{0}".format(cmd_str))
                    response = create_parking_lot(int(cmd_list[1]))
                    print(response)
                elif cmd_list[0] == "leave":
                    # print("ur input is :{0}".format(cmd_str))
                    response = leave_the_vehicle(slot_number=int(cmd_list[1]))
                    print(response)
                elif cmd_list[0] == "registration_numbers_for_cars_with_colour":
                    # print("ur input is :{0}".format(cmd_list))
                    response = find_registration_numbers_for_cars_with_colour(color=cmd_list[1])
                    display_formating_for_list(response)
                elif cmd_list[0] == "slot_numbers_for_cars_with_colour":
                    # print("ur input is :{0}".format(cmd_str))
                    response = find_slot_numbers_for_cars_with_colour(color=cmd_list[1])
                    display_formating_for_list(response)
                elif cmd_list[0] == "slot_number_for_registration_number":
                    # print("ur input is :{0}".format(cmd_str))
                    response = find_slot_number_for_registration_number(reg_num=cmd_list[1])
                    print(response)

            elif len(cmd_list) == 3:
                if cmd_list[0] == "park":
                    # print("ur input is :{0}".format(cmd_str))
                    # print("ur input is :{0}, {1}, {2}".format(cmd_list[0], cmd_list[1], cmd_list[2]))
                    response = park(reg_num=cmd_list[1], color=cmd_list[2])
                    print(response)
                    # park(reg_num, color)
                    # park KA-01-P-333 White

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
