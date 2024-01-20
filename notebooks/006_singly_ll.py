## Singly LL
class Node:
    # Initialize the node object
    def __init__(self, data):  # data is the value of the node
        self.data = data  # Assign data
        self.ref = None  # Initialize next as null


# node1 = Node(10)
# print(node1.data)


# Linked List
class LinkedList:
    def __init__(self):  # Initialize the head of the linked list
        self.head = None  # Initially head is null

    # traversal
    def print_LL(self):
        if self.head is None:
            print("Linked List is empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data,"--->", end=" ")
                n = n.ref
            print(" None", end=" ")

    # add at beginning
    def add_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.ref = self.head
            self.head = new_node

    # add at end
    def add_end(self, data):
        new_node = Node(data)
        n = self.head # copy of head
        if self.head is None:
            self.head = new_node
        else:
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    # add at after the given node
    def add_after(self, data, pos):
        new_node = Node(data)
        n = self.head
        if self.head is None:
            self.head = new_node
        else:
            while n is not None:
                if n.data == pos:
                    break
                n = n.ref
            new_node.ref = n.ref
            n.ref = new_node
            

    # add at before the given node
    def add_before(self, data, pos):
        new_node = Node(data)
        n = self.head
        if self.head is None:
            self.head = new_node
        elif self.head.data == pos:
            new_node.ref=self.head
            self.head=new_node
        else:
            while n is not None:
                if n.ref.data == pos:
                    break
                n = n.ref
            new_node.ref = n.ref
            n.ref = new_node

print()
LL1 = LinkedList()
LL1.print_LL()
LL1.add_begin(10)
LL1.print_LL()
print()
LL1.add_begin(20)
LL1.print_LL()
print()
LL1.add_begin(30)
LL1.print_LL()
print()
LL1.add_end(50)
LL1.print_LL()
print()
LL1.add_end(60)
LL1.print_LL()
print()
# LL1.add_after(40, 20)
# LL1.print_LL()
# print()
# LL1.add_before(25, 20)
# LL1.print_LL()
# print()