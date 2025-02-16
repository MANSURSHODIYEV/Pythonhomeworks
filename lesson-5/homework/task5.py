def is_prime(n):
    """Returns True if n is a prime number, otherwise False."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example usage
num = int(input("Enter a positive integer: "))
print(f"{num} is prime: {is_prime(num)}")

