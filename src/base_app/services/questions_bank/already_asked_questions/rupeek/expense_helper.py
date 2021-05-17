from group_helper import is_contributor_member_of_the_group
import networkx as nx
G=nx.Graph()


class ExpenseIndividual:
    pass


class ExpenseGroup:
    # def __init__(self):
    #     pass
    # def is_contributor_member_of_the_group(self,user_id,group_id):
    #     if is_member_exists(user_id) and is_group_exists(group_id):


    def add_expense(self,contributor_id,group_id,amount):
        self.contributor_id = contributor_id
        self.group_id = group_id
        global dict_group_name
        if is_contributor_member_of_the_group:
            dict_group_name[group_id]


