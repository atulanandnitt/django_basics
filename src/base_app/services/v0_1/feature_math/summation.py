class Summation:
    def addition(self, request_data):
        for key, val in request_data.items():
            sol += int(val)
        return sol
        # print("sum value is : ", a+b)
        # return a+b