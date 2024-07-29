# Input two numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Initialize variables for the Euclidean algorithm
a = num1
b = num2

# Apply the Euclidean algorithm to find the GCD
while b != 0:
    a, b = b, a % b
=
# Print the result
print(f"The greatest common divisor of {num1} and {num2} is: {a}")
