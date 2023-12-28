# 2-Dimensional Array
row_size = int(input("Enter the number of rows:"))
col_size = int(input("Enter the number of columns:"))

# declare a 2-D array
array  = [[0 for j in range(col_size)] for i in range(row_size)]

# ask the user to enter the array elements
print("\nEnter", row_size, "rows and", col_size, "columns:\n")

# loop to store the array elements
for i in range(row_size):
    for j in range(col_size):
        # to store the array element
        element = input()
        # store the element to the array
        array[i][j] = element

# print the array
print("The array is:")
# loop to print the array elements
for i in range(row_size):
    for j in range(col_size):
        # print the array element
        print(array[i][j], end=" ")
    # print a new line
    print()