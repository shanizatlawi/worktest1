# Input a number and a digit from the user
number = input("Enter a number: ")
digit = input("Enter a digit to check: ")

# Check if the digit is a single character and a digit
if len(digit) != 1 or not digit.isdigit():
    print("The digit input is invalid. Please enter a single digit.")
else:
    # Check if the digit appears in the number
    if digit in number:
        print(True)
    else:
        print(False)
