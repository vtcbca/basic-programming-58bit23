# Method 3: Using reversed() and join()
def is_palindrome(s):
    s = s.replace(" ", "").lower()  # Remove spaces and make lowercase
    return s == ''.join(reversed(s))

input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
