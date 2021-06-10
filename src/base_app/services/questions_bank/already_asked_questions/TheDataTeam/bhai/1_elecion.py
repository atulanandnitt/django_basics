
def election(candidates):
    """

    :param candidates:
    :return:
    """
    # voting = set()
    votes = dict()
    votes = {key:candidates.count(key) for key in set(candidates)}
    # for name in candidates:
    #     if votes.get(name) is None:
    #         votes[name] = 1
    #     else:
    #         votes[name] += 1

    max_vote = 0
    winner = None
    for key, value in votes.items():
        # print(key, value)
        if value >= max_vote:
            max_vote = value
            if winner is None or key > winner:
                # key > winner to assure alphabetical order
                winner = key
                # print("temp winner is : {0}".format(winner))

    print(votes)
    print(winner, max_vote)


election(['Alex', 'Michael', 'Harry', 'Dave', 'Michael', 'Victor', 'Harry', 'Alex', 'Mary', 'Mary']) #Q1

election(['Mary', 'Mary','Alex', 'Michael', 'Harry', 'Dave', 'Michael', 'Victor', 'Harry', 'Alex']) #Q1
