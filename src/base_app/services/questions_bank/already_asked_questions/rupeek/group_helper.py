dict_group_name = dict()
from sign_up import is_member_exists

class CreateGroup:
    # def __init__(self, creator, group_member):
    #     self.creator = creator
    #     self.group_member = group_member

    def is_group_exists(self, group_details):
        return False

    def is_all_users_exists(self, group_details):
        return True
        # display_all_reg_users

    def add_group(self, group_details):
        print("adding new group : {0}".format(group_details))
        if self.is_group_exists(group_details):
            return "group already exists, can't create the same name group"

        if self.is_all_users_exists(group_details):
            try:
                print("group_details : {0}".format(group_details))
                print(group_details["Name"], group_details["Users"])

                dict_group_name[group_details["Name"]] = group_details
            except ValueError as err:
                raise ("ValueError in finding add_group : {0}".format(err.args))


class AddMemberInTheExistingGroup:
    def is_member_reg_user(self,member_phone):
        return True

    def is_group_exists(self, group_name):
        return True

    def add_member(self, member_phone, group_name):
        if self.is_member_reg_user(member_phone) \
                and self.is_group_exists(group_name):
            print("preconditions satisfied")
            dict_group_name[group_name]["Users"].append(member_phone)


def display_all_reg_groups():
    print("total number of groups : {0}".format(len(dict_group_name)))
    print("list of all the groups is : ")
    for key,val in dict_group_name.items():
        print("group name : {0} and group details : {1}".format(key,val))


def is_group_exists(group_id):
    if dict_group_name.has_key(group_id):
        return True
    else:
        return False


def is_contributor_member_of_the_group(user_id, group_id):
    if is_group_exists(group_id) and is_member_exists(user_id):
        if user_id in dict_group_name[group_id]["Users"]:
            return True
    return False




class ExitAUser:
    def __init__(self, user_id, group_id):
        # user_id is phone for simplicity
        # user_id is group_name for simplicity
        self.user_id = user_id
        self.group_id = group_id

    def is_user_exist(self):
        return True

    def is_debt_settled(self):
        return True

    def remove_a_user(self):
        if self.is_user_exist() and self.is_debt_settled():
            idx = dict_group_name[self.group_id]["Users"].index(self.user_id)
            dict_group_name[self.group_id]["Users"].pop(idx)

