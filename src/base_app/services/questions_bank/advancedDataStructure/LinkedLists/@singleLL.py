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

    def detect_loop(self):
        slow = self.head
        fast = self.head
        while fast is not None:
            slow = slow.next
            if fast.next and fast.next.next:
                temp = fast
                fast=fast.next.next
            else: return False

            # try:
            #     fast = fast.next.next
            # except:
            #     return False

            if fast == slow:
                return True
        else:
            return False

    def create_a_loop(self):
        self.head.next.next.next.next.next.next = self.head

    def remove_loop(self):
        slow = self.head
        fast = self.head
        while fast is not None:
            slow = slow.next
            if fast.next and fast.next.next:
                temp = fast
                fast=fast.next.next
            else: return False

            if fast == slow:
                temp.next.next = None
                print("loop detected and removed the loop")
        else:
            return False
    
    def add_math_ll(self):
        pass

ll = LinkedList()
list1 = [1,3,5,7,9,11,7]
for item in list1:
    ll.add_node(item)

ll.display()

ll.rev()
print("after rev: ")
ll.display()
print("detect_loop(self) : ", ll.detect_loop())


print("create_a_loop(self) : ", ll.create_a_loop())
print("detect_loop(self) : ", ll.detect_loop())

print("remove_loop(self) : ", ll.remove_loop())
print("after remove_loop: ", ll.display())