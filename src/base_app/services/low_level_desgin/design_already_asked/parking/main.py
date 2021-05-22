import sys
import helper

# reg_number_and_colour = dict()
# reg_number_and_slot_number = dict()
# colour_and_slot_number = dict()
# size_of_the_parking = 0
# occupancy_array = list()


def execute_cmd(cmd_str, parking_obj):
    if cmd_str == "exit":
        exit()

    else:
        cmd_list = cmd_str.split()

        if len(cmd_list) == 1 and cmd_list[0] == "status":
            parking_obj.find_status()

        elif len(cmd_list) == 2:
            if cmd_list[0] == "create_parking_lot":
                response = parking_obj.create_parking_lot(int(cmd_list[1]))
                print(response)

            elif cmd_list[0] == "leave":
                response = parking_obj.leave_the_vehicle(slot_number=int(cmd_list[1]))
                print(response)

            elif cmd_list[0] == "registration_numbers_for_cars_with_colour":
                response = parking_obj.find_registration_numbers_for_cars_with_colour(colour=cmd_list[1])
                formatted_response = helper.display_formatting(response)
                print(formatted_response)

            elif cmd_list[0] == "slot_numbers_for_cars_with_colour":
                response = parking_obj.find_slot_numbers_for_cars_with_colour(colour=cmd_list[1])
                formatted_response = helper.display_formatting(response)
                print(formatted_response)

            elif cmd_list[0] == "slot_number_for_registration_number":
                response = parking_obj.find_slot_number_for_registration_number(reg_number=cmd_list[1])
                print(response)

        elif len(cmd_list) == 3:
            if cmd_list[0] == "park":
                response = parking_obj.park(reg_number=cmd_list[1], colour=cmd_list[2])
                print(response)

        else:
            print("it was incorrect cmd, Enter correct command")


def run_as_interactive_input(parking_obj):
    while 1:
        cmd_str = input()
        execute_cmd(cmd_str, parking_obj)


def run_as_per_file_input(file_name, parking_obj):
    with open(file_name, "r") as f1:
        data = f1.readlines()

    for cmd_str in data:
        execute_cmd(cmd_str, parking_obj)


def main():
    parking_obj = helper.Parking()
    if len(sys.argv) > 1:
        run_as_per_file_input(sys.argv[1], parking_obj)
    else:
        run_as_interactive_input(parking_obj)


if __name__ == '__main__':
    main()