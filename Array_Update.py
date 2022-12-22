# Array Update

# array declaration and initialization
array = [20, 10, 30, 15, 25]

# print the array
print("The array is:")
# loop to print the array elements
for i in array:
    # print the array element
    print(i, end=" ")

# ask the user to enter the element to update
update_ele = input("\nEnter the element to update : ")

# ask the user to enter the new element
new_ele = input("Enter the new element : ")

# check if the element is in the array
if update_ele in array:
    # get the index of the updating element
    index = array.index(update_ele)
    # update the element
    array[index] = new_ele
    # print array update message
    print("Element updated successfully in the array")
    # print the array
    print("The array is:")
    # loop to print the array elements
    for i in array:
        # print the array element
        print(i, end=" ")
else:
    print("Element not found in the array")