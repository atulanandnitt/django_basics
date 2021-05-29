class Node:
    def __init__(self, val=0):
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

    def odd_even_ll(self) -> Node:
        # TODO: ???
        # https://www.youtube.com/watch?v=QcSLh0JtwFk&list=PLYAlGR1wWgUU75tRZfDFEorFstOrRGAoV&index=20
        # https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3331/
        for_odd = self.head
        for_even = self.head
        temp = self.head
        odd_head = for_odd
        even_head = for_even
        is_odd = True
        while temp:
            if is_odd:
                for_odd.next = temp
                for_odd = for_odd.next
                print("displaying the ll: ", end="")
                self.display()
            else:
                for_even.next = temp
                for_even = for_even.next
            is_odd = not is_odd
            temp = temp.next
        for_even.next = None
        for_odd.next = even_head.next
        return odd_head.next

ll = LinkedList()
# list1 = [1,3,5,7,9,11,7]
list1 = range(11)
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


head = ll.odd_even_ll()
print("ll.display() after ll.odd_even_ll(): ", ll.display())