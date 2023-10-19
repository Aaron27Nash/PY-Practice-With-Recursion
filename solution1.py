# Write code for algorithm 1 below:

    # Base case: if n is less than 0, stop the recursion
def print_numbers(n) :
  if n < 0:
        return
    
    # Print the current number
        print(n)
    
    # Call the function recursively with n-1
        print_numbers(n - 1)

# Example usage:
print_numbers(5)
