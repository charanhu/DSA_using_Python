# Array Deletion

# ask array size
num = int(input("Enter the Array Size : "))

# declare an array
array = []

# ask the user to enter the array elements
print("\nEnter", num, "elements:\n")
# loop to store the array elements
for i in range(num):
    # element to store the array element
    element = input()
    # append the element to the array
    array.append(element)

# to delete an elemnt
# ask the user to enter the element to delete
del_ele = input("Enter the element to delete : ")

#check if the element is in the array
if del_ele in array:
    # remove the element from the array
    array.remove(del_ele)
    # print array deletion message
    print("Element deleted successfully from the array")
    # decrement the array size
    num = num - 1
    # print the array
    print("The array is:")
    # loop to print the array elements
    for i in range(num):
        # print the array element
        print(array[i], end=" ")
else:
    print("Element not found in the array")