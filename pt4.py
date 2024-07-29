# Input two numbers
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Initialize the product to 0
    product = 0

    # Initialize a counter for the while loop
    count = 0

    # Use a while loop to compute the product
    while count < abs(num2):  # Repeat until count reaches the absolute value of num2
        product += num1
        count += 1

    # Handle negative numbers
    if num2 < 0:
        product = -product

    # Print the result
    print(f"The product of {num1} and {num2} is: {product}")

except ValueError:
    print("Invalid input. Please enter integer values.")
