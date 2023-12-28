# Array Sort

# array declaration and initialization
array = [20, 10, 30, 15, 25]

# print the array
print("The array is:")
# loop to print the array elements
for i in array:
    # print the array element
    print(i, end=" ")


# sort the array
for i in range(len(array)):
    for j in range(i+1, len(array)):
        if array[i] > array[j]:
            temp = array[i]
            array[i] = array[j]
            array[j] = temp

# print the array
print("\nThe sorted array is:")
# loop to print the array elements
for i in array:
    # print the array element
    print(i, end=" ")