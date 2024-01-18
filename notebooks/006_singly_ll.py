## Singly LL
class Node:
    # Initialize the node object
    def __init__(self, data): # data is the value of the node
        self.data = data # Assign data
        self.ref = None # Initialize next as null

# node1 = Node(10)
# print(node1.data)


# Linked List
class LinkedList:
    def __init__(self): # Initialize the head of the linked list
        self.head = None # Initially head is null

    #traversal
    def print_LL(self): 
        if self.head is None:
            print("Linked List is empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

LL1 = LinkedList()
LL1.print_LL()