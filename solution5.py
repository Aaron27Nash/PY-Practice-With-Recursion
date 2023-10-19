# Write code for algorithm 5 below
def is_palindrome(s):
    # Base case: an empty string or a single character string is a palindrome
    if len(s) <= 1:
        return True
    else:
        # Recursive case: check if the first and last characters are the same
        return s[0] == s[-1] and is_palindrome(s[1:-1])

# Example usage:
result1 = is_palindrome("madam")
result2 = is_palindrome("hello")

print(f"'madam' is a palindrome: {result1}")  # Output: 'madam' is a palindrome: True
print(f"'hello' is a palindrome: {result2}")  # Output: 'hello' is a palindrome: False
