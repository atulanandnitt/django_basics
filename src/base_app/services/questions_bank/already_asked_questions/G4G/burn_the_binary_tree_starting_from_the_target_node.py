


class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def create_bst(self,val):
        if self.root == None:
            self.root = Node(val)
        else:
            tmp = self.root
            while tmp.data > val:
                if tmp.left:
                    tmp = tmp.left
                else:
                    tmp.left = Node(val)
                    break

            while tmp.data < val:
                if tmp.right:
                    tmp = tmp.right
                else:
                    tmp.right = Node(val)
                    break
        # return self.root

    def disp(self,tmp):
        if tmp:
            self.disp(tmp.left)
            print(tmp.data)
            self.disp(tmp.right)

    def bfs(self, tmp):
        q = list()
        q.append(tmp)
        while len(q) > 0:
            t1 = q.pop(0)
            print("data is :",t1.data)
            if t1.left:
                q.append(t1.left)

            if t1.right:
                q.append(t1.right)


    def burn_the_binary_tree_starting_from_the_target_node(self,temp):
        pass


bst = BST()
list1 = [12, 13, 10, 14, 15, 21, 24, 22, 23]
for item in list1:
    bst.create_bst(item)

bst.disp(bst.root)
bst.bfs(bst.root)
