class Node:
    def __init__(self, val):
        self.next = None
        self.data = val

class LinkedList:

    def __init__(self):
        self.head = None
    
    def add_node(self, val):
        if self.head is None:
            self.head = Node(val)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(val)
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, "" , end="")
            temp = temp.next

    def rev(self):
        p = self.head
        q = p.next
        r = p.next
        p.next = None
        while 1:
            if r.next:
                r = r.next
            q.next = p
            p = q
            q = r
            if q.next is None:
                q.next = p
                self.head = q
                break            

    
ll = LinkedList()
list1 = [1,3,5,7,9,11]
for item in list1:
    ll.add_node(item)

ll.display()

ll.rev()
print("after rev: ")
ll.display()