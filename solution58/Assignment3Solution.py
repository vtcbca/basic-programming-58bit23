def fibonacci_while_loop(max_value):
    fib_sequence = []
    a, b = 0, 1
    while a <= max_value:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Test the function
max_val = int(input("Enter the maximum value: "))
print(f"Fibonacci sequence (up to {max_val}): {fibonacci_while_loop(max_val)}")