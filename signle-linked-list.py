class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def print_ll(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "--->", end=" ")
                n = n.ref
    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
    def add_after(self, data, x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print("node is not present in LL")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    def add_before(self, data, x):
        n = self.head
        if n is None:
            print("Node is not present is")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("Node is not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked list is not empty")
    def delete_start(self):
        if self.head is None:
            print("LL is empty")
        else:
            self.head = self.head.ref
    def delete_end(self):
        n = self.head
        if n is None:
            print("LL is empty")
        elif self.head.ref is None:
            self.head = None
        else:            
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None
    def delete_by_position(self, x):
        if self.head is None:
            print("LL is empty")
            return
        if self.head.data == x:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("Noe is not found!!!")
        else:
           n.ref = n.ref.ref  

LL1 = LinkedList()
LL1.add_begin(500)
LL1.add_begin(600)
LL1.add_begin(700)
# LL1.add_after(800, 500)
# LL1.add_before(700, 800)
# LL1.add_before(400, 500)
# LL1.add_begin(300)
# LL1.insert_empty(200)

# delete nodes
# LL1.delete_start()
# LL1.delete_end()
LL1.delete_by_position(500)
LL1.print_ll()
    
