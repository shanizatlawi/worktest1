# Input two numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Initialize result to 0
result = 0

# Use a loop to add num1 to itself num2 times
while num2 > 0:
    # If num2 is odd, add num1 to result
    if (num2 % 2) == 1:
        result = result + num1

    # Double num1 and halve num2
    num1 = num1 * 2
    num2 = num2 // 2

# Print the result
print("The result of multiplying is:", result)
