# Method 3: Using List Comprehension
def print_pattern(n):
    for i in range(1, n + 1):
        print(' '.join(['*'] * i))

input_lines = int(input("Enter number of lines: "))  # Input number of lines
print_pattern(input_lines)
