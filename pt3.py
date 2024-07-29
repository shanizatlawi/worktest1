# Initialize variables to store numbers and their serial numbers
numbers = []
serial_numbers = []

# Loop to take 5 numbers from the user
for i in range(1, 6):
    while True:
        try:
            # Prompt the user to enter a number
            number = float(input(f"Enter number {i}: "))
            numbers.append(number)
            serial_numbers.append(i)  # Store the serial number of the input
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Find the index of the highest number
max_index = numbers.index(max(numbers))

# Display the serial number of the highest value
print(f"The serial number of the highest value is: {serial_numbers[max_index]}")
