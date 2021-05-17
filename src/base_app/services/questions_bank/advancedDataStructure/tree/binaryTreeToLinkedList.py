class NodeLL:
    def __init__(self,val):
        self.data = val
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def addNode(self, val):
        if self.head is None:
            self.head = NodeLL(val)

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = NodeLL(val)

    def display(self, temp):
        while temp:
            print(temp.data)
            temp = temp.next


class Node(object):

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Tree(object):

    def __init__(self):
        self.root = None

    def addNode(self, val):
        if self.root is None:
            self.root = Node(val)

        else:
            temp = self.root
            while 1:
                if temp.data < val:
                    if temp.right:
                        temp = temp.right
                    else:
                        temp.right = Node(val)
                        break

                elif temp.data > val:
                    if temp.left:
                        temp = temp.left
                    else:
                        temp.left = Node(val)
                        break

                if temp.data == val:
                    print("duplicates not allowed in the tree ")

    def inorder(self, temp):
        # print("inside inorder")
        if temp:
            self.inorder(temp.left)
            print(temp.data)
            self.inorder(temp.right)

t1 = Tree()
list1 = [5, 7, 3, 8, 1, 9, 2]
for item in list1:
    t1.addNode(item)

t1.inorder(t1.root)


ll = linkedList()
list2 = [5, 7, 3, 8, 1, 9, 2]
for item in list2:
    ll.addNode(item)

ll.display(ll.head)


mat = [[i for i in range(3)] for j in range(3)]
print("mat : ", mat)

# mat2=[0 for i in range(3) [0 for j in range(3)]]
# print(mat2)

mat3= list()
n=3
for i in range(n):
    temp = list()
    for j in range(n):
        temp.append((i*n) + j)
    mat3.append(temp)
print(mat3)

n=3
mat4 =[[0 for i in range(n)] for j in range(n)]
print(mat4)