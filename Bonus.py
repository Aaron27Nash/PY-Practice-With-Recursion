def gcd(a, b):
    # Base case: if b is 0, then a is the GCD
    if b == 0:
        return a
    else:
        # Recursive case: recursively call gcd with b and a % b (remainder of a divided by b)
        return gcd(b, a % b)

# Example usage:
result = gcd(15, 10)
print(f"The greatest common divisor of 15 and 10 is: {result}")  # Output: The greatest common divisor of 15 and 10 is: 5
