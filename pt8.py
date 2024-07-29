import math

# Input a number from the user
num = int(input("Enter a number: "))

# Edge case for numbers less than or equal to 1
if num <= 1:
    print(f"{num} is not a prime number.")
else:
    # Assume the number is prime until proven otherwise
    is_prime = True

    # Check divisibility from 2 up to the square root of the number
    if num > 3:
        if num % 2 == 0 or num % 3 == 0:
            is_prime = False
        else:
            i = 5
            while i * i <= num:
                if num % i == 0 or num % (i + 2) == 0:
                    is_prime = False
                    break
                i += 6

    # Print the result based on the is_prime flag
    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
