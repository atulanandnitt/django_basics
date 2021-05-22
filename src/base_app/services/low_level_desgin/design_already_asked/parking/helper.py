class Car:
    def __init__(self, colour, reg_number):
        self.colour = colour
        self.reg_number = reg_number


def display_formatting(data):
    str_format = ""
    for item in data[:-1]:
        str_format += str(item) + ", "
    str_format += str(data[-1])
    return str_format


class Parking:

    def __init__(self):
        self.occupancy_array = list()
        self.size_of_the_parking = 0
        self.reg_number_and_colour = dict()
        self.reg_number_and_slot_number = dict()
        self.colour_and_slot_number = dict()

    def create_parking_lot(self, n):
        self.size_of_the_parking = n
        self.occupancy_array = [None for _ in range(self.size_of_the_parking)]
        return "Created a parking lot with {0} slots".format(int(self.size_of_the_parking))

    def find_status(self):
        print("Slot No.    Registration No    Colour")
        for i in range(len(self.occupancy_array)):
            if self.occupancy_array[i]:
                print("{0}           {1}      {2}".format(str(i + 1), self.occupancy_array[i].reg_number,
                                                          self.occupancy_array[i].colour))

    def is_parking_full(self):
        for i in range(len(self.occupancy_array)):
            if self.occupancy_array[i] is None:
                return False
        else:
            return True

    def find_nearest_slot_avl(self):
        for i in range(len(self.occupancy_array)):
            if self.occupancy_array[i] is None:
                slot_number = i + 1
                return slot_number

    def park(self, reg_number, colour):

        if self.is_parking_full():
            return "Sorry, parking lot is full"
        else:
            c1 = Car(colour, reg_number)
            slot_number = self.find_nearest_slot_avl()
            reg_number_list = [reg_number]
            slot_number_list = [slot_number]

            try:
                self.reg_number_and_colour[colour].append(reg_number)
            except KeyError:
                self.reg_number_and_colour[colour] = reg_number_list
            except ValueError as err_msg:
                raise ValueError("problem in park while adding self.reg_number_and_colour :{0}".format(str(err_msg)))

            try:
                self.reg_number_and_slot_number[reg_number] = slot_number
            except KeyError:
                print(""" reg number is unique so if a car with the particular reg number is
                           already parked it cant be parked again untll or unless its gone out""")
            except ValueError as err_msg:
                raise ValueError("problem in park while adding self.reg_number_and_slot_number: {0}".format(err_msg))

            try:
                self.colour_and_slot_number[colour].append(slot_number)
            except KeyError:
                self.colour_and_slot_number[colour] = slot_number_list
            except ValueError as err_msg:
                raise ValueError("problem in park while adding self.colour_and_slot_number: {0}".format(err_msg))

            slot_number = self.find_nearest_slot_avl()
            self.occupancy_array[slot_number - 1] = c1
            return "Allocated slot number: {0}".format(slot_number)

    def is_vehicle_present(self, slot_number):
        if self.occupancy_array[slot_number]:
            return True
        else:
            return False

    def leave_the_vehicle(self, slot_number):
        if self.is_vehicle_present(slot_number - 1):
            self.occupancy_array[slot_number - 1] = None
            return "Slot number {0} is free".format(slot_number)
        else:
            return "Sorry, No vehicle at slot_number:{0}".format(slot_number)

    def find_registration_numbers_for_cars_with_colour(self, colour):
        try:
            reg_numbers = self.reg_number_and_colour[colour]
            return reg_numbers
        except KeyError:
            return "Not found"
        except ValueError as err_msg:
            raise ValueError("problem in find_registration_numbers_for_cars_with_colour :{0}".format(str(err_msg)))

    def find_slot_numbers_for_cars_with_colour(self, colour):
        try:
            list_of_reg_number = self.colour_and_slot_number[colour]
            return list_of_reg_number
        except ValueError as err_msg:
            raise ValueError("problem in find_slot_numbers_for_cars_with_colour :{0}".format(err_msg))

    def find_slot_number_for_registration_number(self, reg_number):
        try:
            slot_number = self.reg_number_and_slot_number[reg_number]
            return slot_number
        except KeyError:
            return "Not found"
        except ValueError as err_msg:
            raise ValueError("problem in find_slot_number_for_registration_number: {0}".format(err_msg))
