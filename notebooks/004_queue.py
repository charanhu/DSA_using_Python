# QUEUES
queue = [] # empty queue

# Inserting elements into the queue
def enqueue(x):
    element = input("Enter the element to be inserted: ")
    queue.append(element) # insert element at the end of the queue
    print(element, "is inserted into the queue")

# Removing elements from the queue
def dequeue():
    # Check if the queue is empty
    if not queue:
        print("Queue is empty")
    else:
        e = queue.pop(0) # remove the first element from the queue
        print("Removed element: ", e)

# Displaying the elements in the queue
def display():
    # Check if the queue is empty
    if not queue:
        print("Queue is empty")
    else:
        print(queue)

# Menu driven program
while True:
    print("Select the operation 1. ADD 2. REMOVE 3. DISPLAY 4. EXIT")
    choice = int(input())
    if choice == 1:
        enqueue(queue)
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print("Invalid choice")
