# stack implementaion using LIST

# stack of size 5
stack = [None] * 5 # None is a special value in Python that represents nothingness

# declare top of stack
top = -1

# inserting elements in stack
def push():
    global top
    if top == len(stack) - 1:
        print("Stack is full")
    else:
        top = top + 1
        push = input("Enter the element to push : ")
        stack[top] = push

# deleting elements from stack
def pop():
    global top
    if top == -1:
        print("Stack is empty")
    else:
        print("Element popped from stack is : ", stack[top])
        top = top - 1

# display the stack
def display():
    if top == -1:
        print("Stack is empty")
    else:
        print("Stack is : ")
        for i in range(top, -1, -1):  # parameter of range() function is start, stop, step
            print(stack[i], end=" ")
        print()

# main function
def main():
    while True:
        print("1. Push")
        print("2. Pop")
        print("3. Display")
        print("4. Exit")
        choice = int(input("Enter your choice : "))
        if choice == 1:
            push()
        elif choice == 2:
            pop()
        elif choice == 3:
            display()
        elif choice == 4:
            break
        else:
            print("Invalid choice")

# call the main function
if __name__ == "__main__":
    main()
