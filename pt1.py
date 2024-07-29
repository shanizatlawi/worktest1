numbers = []  # List to store the entered numbers

while True:
    number = int(input("Enter a number (or -99 to stop): "))
    if number == -99:
        if numbers:  # Check if the list is not empty
            print("Sum of numbers:", sum(numbers))
        else:
            print("None")
        break
    numbers.append(number)
