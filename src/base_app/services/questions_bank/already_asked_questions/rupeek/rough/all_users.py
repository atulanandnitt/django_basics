#
# class Details_of_all_users:
#
#     def __init__(self):
#         self.dict_phone = dict()
#         self.dict_email = dict()
#
#     def is_user_exists(self, user_details):
#         return False
#         # try:
#         #     if self.dict_phone[user_details.Phone] or self.dict_email[user_details.Email]:
#         #         return True
#         #     else:
#         #         return False
#         # except ValueError as err:
#         #     raise ("ValueError in finding is_user_exists : {0}".format(err.args))
#
#
#     def add_new_user(self, user_details):
#         try:
#             new_user_details = user_details
#             print("user_details : {0}".format(user_details))
#             print(user_details["Name"], user_details["Phone"],user_details["Email"])
#             phone = user_details["Phone"]
#             self.dict_phone[phone] = new_user_details
#             self.dict_email[user_details["Email"]] = new_user_details
#         except ValueError as err:
#             raise ("ValueError in finding is_user_exists : {0}".format(err.args))
#         # except:
#         #     raise ("issue in finding is_user_exists ")
#
#     def display_all_users(self):
#         print("total number of users : {0}".format(len(self.dict_phone)))
#         print("list of all the users is : ")
#         for key,val in self.dict_phone.items():
#             print("phone : {0} and user details : {1}".format(key,val))


dict1 = {"1":"one"}
print(dict1["2"])
