# Write code for algorithm 3 below
def fibonacci(n):
    # Base cases: 
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive case: Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2)
        return fibonacci(n-1) + fibonacci(n-2)

# Example usage:
result_n4 = fibonacci(4)
result_n2 = fibonacci(2)

print(f"The 4th Fibonacci number is: {result_n4}")  # Output: The 4th Fibonacci number is: 2
print(f"The 2nd Fibonacci number is: {result_n2}")  # Output: The 2nd Fibonacci number is: 1
