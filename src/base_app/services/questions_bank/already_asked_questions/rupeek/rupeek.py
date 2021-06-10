from sign_up import Signup
from sign_up import display_all_reg_users
from group_helper import CreateGroup
from group_helper import AddMemberInTheExistingGroup
from group_helper import display_all_reg_groups
from group_helper import ExitAUser

# import logging
# logger = logging.getLogger()
# logger.info("info logged")

def main():
    new_user_details = {
        "Name" : "Test User",
        "Phone" : "9999999991",
        "Email" : "abcd.com"
    }
    singup_obj = Signup()
    response_1 = singup_obj.add_user(new_user_details)
    if response_1 == "Success":
        print("user signed up successfully")
    new_user_details_2 = {
        "Name" : "Test User2",
        "Phone" : "9999999992",
        "Email" : "abcd_2.com"
    }
    response_2 = singup_obj.add_user(new_user_details_2)
    if response_2 == "Success":
        print("user signed up successfully")
    new_user_details_3 = {
        "Name" : "Test User_3",
        "Phone" : "9999999993",
        "Email" : "abcd_3.com"
    }
    response_3 = singup_obj.add_user(new_user_details_3)

    if response_3 == "Success":
        print("user signed up successfully")
    display_all_reg_users()

    new_group_details = {
        "Name" : "Group1",
        "Users": ["9999999991", "9999999992"],
    }
    create_group = CreateGroup()
    create_group.add_group(new_group_details)
    display_all_reg_groups()

    add_group_mem=AddMemberInTheExistingGroup()
    add_group_mem.add_member("9999999993","Group1")
    display_all_reg_groups()

    exit_a_user = ExitAUser("9999999991","Group1")
    exit_a_user.remove_a_user()
    display_all_reg_groups()

if __name__ == '__main__':
    main()
