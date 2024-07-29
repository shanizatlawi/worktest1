# Initialize an empty list to store the numbers
numbers = []

while True:
    # Prompt the user to enter a number
    user_input = input("Enter a number (or a negative number or '.0' to stop): ")

    # Convert input to a float
    try:
        number = float(user_input)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    # Check if the input is -99
    if number == -99:
        if numbers:
            highest = max(numbers)
            lowest = min(numbers)
            print(f"Highest value recorded: {highest}")
            print(f"Lowest value recorded: {lowest}")
        else:
            print("None")
        break

    # Check if the input is a negative number or .0
    if number < 0 or number == 0:
        if numbers:
            highest = max(numbers)
            lowest = min(numbers)
            print(f"Highest value recorded: {highest}")
            print(f"Lowest value recorded: {lowest}")
        else:
            print("None")
        break

    # Append the valid number to the list
    numbers.append(number)
