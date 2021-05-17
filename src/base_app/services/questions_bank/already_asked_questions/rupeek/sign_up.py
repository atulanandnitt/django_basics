dict_phone = dict()
dict_email = dict()

class Signup:
    # def __init__(self):
    #     dict_phone = dict()
    #     dict_email = dict()

    # def is_user_exists(self, user_details):
    #     return False
        # try:
        #     if dict_phone[user_details["Phone"]] or dict_email[user_details["Email"]]:
        #         return True
        #     else:
        #         return False
        # except ValueError as err:
        #     raise ("ValueError in finding is_user_exists : {0}".format(err.args))

    def is_user_exists(self,user_details):
        user_id = user_details["Phone"]
        if dict_phone.has_key(user_id):
            return True
        else:
            return False


    def add_user(self, user_details):
        print("adding new user : {0}".format(user_details))
        if self.is_user_exists(user_details):
            return "user already exists, can't reg"
        else:
            try:
                new_user_details = user_details
                print("user_details : {0}".format(user_details))
                print(user_details["Name"], user_details["Phone"], user_details["Email"])
                phone = user_details["Phone"]
                dict_phone[phone] = new_user_details
                dict_email[user_details["Email"]] = new_user_details
            except ValueError as err:
                raise ("ValueError in finding is_user_exists : {0}".format(err.args))
        return "Success"

    # def verify_user_addition(self, user_details):
    #     check in the dict_phone

def display_all_reg_users():
    print("total number of users : {0}".format(len(dict_phone)))
    print("list of all the users is : ")
    for key,val in dict_phone.items():
        print("phone : {0} and user details : {1}".format(key,val))


def is_member_exists(user_id):
    if dict_phone.has_key(user_id):
        return True
    else:
        return False


# class List(Signup):
#     def get_all_users(self):
