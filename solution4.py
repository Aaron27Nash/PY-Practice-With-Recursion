# Write code for algorithm 4 below
def power(a, b):
    # Base case: any number raised to the power of 0 is 1
    if b == 0:
        return 1
    else:
        # Recursive case: a^b = a * a^(b-1)
        return a * power(a, b - 1)

# Example usage:
result = power(2, 4)
print(f"2 raised to the power of 4 is: {result}")  # Output: 2 raised to the power of 4 is: 16
