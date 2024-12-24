# Method 3: Using List Comprehension for Numbers
def print_triangle(n):
    for i in range(1, n+1):
        # Create the row using list comprehension
        row = ' '.join([str(x) for x in range(1, 2*i)])
        # Print leading spaces and the row
        print(' ' * (n - i) + row)

input_lines = int(input("Enter the number of rows: "))  # Input number of rows
print_triangle(input_lines)
