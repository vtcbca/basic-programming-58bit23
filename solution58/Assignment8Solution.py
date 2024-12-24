# Method 3: Using List Comprehension for Characters
def print_pattern(n):
    for i in range(1, n+1):
        # Create the increasing part using list comprehension
        increasing_part = [chr(64 + j) for j in range(1, i+1)]
        # Create the decreasing part
        decreasing_part = increasing_part[:-1][::-1]
        
        # Join the parts with spaces and print them with leading spaces
        print(' ' * (n - i) + ' '.join(increasing_part + decreasing_part))

input_lines = int(input("Enter the number of lines: "))  # Input number of rows
print_pattern(input_lines)
