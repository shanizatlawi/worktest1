# Input a number from the user
number = input("Enter a two-digit number: ")

# Check if the input is a two-digit number
if len(number) != 2:
    print("Error: The number is not two digits.")
else:
    # Reverse the digits of the number
    reversed_number = number[::-1]

    # Print the reversed number
    print(f"The reversed number is: {reversed_number}")

