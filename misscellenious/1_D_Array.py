# print statement to ask the array size
print("How many elements do you want to store?:", end="")
# to store the array size
size  = int(input())
# declare an array
array = []
# ask the user to enter the array elements
print("\nEnter", size, "elements:\n")
# loop to store the array elements
for i in range(size):
    # to store the array element
    element = input()
    # append the element to the array
    array.append(element)

# print the array
print("The array is:")
# loop to print the array elements
for i in range(size):
    # print the array element
    print(array[i], end=" ")