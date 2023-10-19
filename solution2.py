# Write code for algorithm 2 below
def print_natural_numbers(n):
    # Base case: if n is less than 1, stop the recursion
    if n < 1:
        return
    
    # Call the function recursively with n-1
    print_natural_numbers(n - 1)
    
    # Print the current number
    print(n)

# Example usage:
print_natural_numbers(5)
