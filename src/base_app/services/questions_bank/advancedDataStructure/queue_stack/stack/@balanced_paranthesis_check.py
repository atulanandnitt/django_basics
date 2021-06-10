
class Stack:

    def __init__(self, limit=10):
        self.stack_custom = list()
        self.MAX_LENGTH = limit

    def pop(self):
        if len(self.stack_custom) > 0:
            temp = self.stack_custom[-1]
            self.stack_custom = self.stack_custom[:-1]
            return temp
        else:
            return -1

    def push(self, data):
        if len(self.stack_custom) < self.MAX_LENGTH:
            self.stack_custom.append(data)
        else:
            print("stack is FULL")
    
    def peek(self):
        if len(self.stack_custom) > 0:
            return self.stack_custom[-1]
        else:
            return -1


def is_opening(item):
    if item in "[{(":
        return True
    else:
        return False

def is_closing(item):
    if item in ")}]":
        return True
    else:
        return False

def reverse_of(temp):
    if temp == "(":
        return ")"
    elif temp == "{":
        return "}"
    elif temp == "[":
        return "]"        

def is_balanced_paranthesis(s1, text):
    for item in text:
        if is_opening(item):
            s1.push(item)
        elif is_closing(item):
            if s1.peek():
                temp = s1.pop()
            else:
                return False
            if item is reverse_of(temp):
                continue
            else:
                return False
    
    if len(s1.stack_custom) == 0:
        counter = text.count("|")
        if counter % 2 == 0:
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    s1 = Stack()
    str1 = "|({[)}]"
    print("running UTs")
    for item in str1:
        assert is_balanced_paranthesis(s1, item) == False
        s1.stack_custom= list()

    open_str = "|({["
    close_str = "|)}]"

    for i in range(len(open_str)):
        for j in range(len(close_str)):
            if i==j:
                assert is_balanced_paranthesis(s1, open_str[i]+close_str[j]) == True
                s1.stack_custom= list()
            else:
                assert is_balanced_paranthesis(s1, open_str[i]+close_str[j]) == False
                s1.stack_custom= list()
