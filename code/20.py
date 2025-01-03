def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def has_three_factors(n):
    # Step 1: Find the square root of the number
    sqrt_n = int(n ** 0.5)
    
    # Step 2: Check if n is a perfect square
    if sqrt_n * sqrt_n != n:
        return False
    
    # Step 3: Check if the square root is a prime number
    return is_prime(sqrt_n)

# Example usage
n = int(input("Enter a number: "))
if has_three_factors(n):
    print(f"The number {n} has exactly three factors.")
else:
    print(f"The number {n} does not have exactly three factors.")
