# Initialize an empty list to store the temperatures
temperatures = []

# Number of months (cards) to process
num_months = 12

for i in range(num_months):
    while True:
        try:
            # Input the temperature for the month
            temp_input = input(f"Enter the temperature for month {i + 1}: ")

            # Convert the input to a float
            temp = float(temp_input)

            # Check for valid temperature range
            if temp < 5 or temp > 40:
                print("Temperature out of range. Please enter a value between 5°C and 40°C.")
                continue

            # Check for consecutive 0°C temperatures and ignore the input
            if len(temperatures) > 0 and temp == 0 and temperatures[-1] == 0:
                print("Consecutive 0°C temperatures are not allowed. Please enter the temperature again.")
                continue

            # Add the valid temperature to the list
            temperatures.append(temp)
            break  # Exit the loop for a valid input

        except ValueError:
            # Handle the case where input is not numeric
            print("Invalid input. Please enter a numeric value.")

# Check if we have exactly 12 temperatures
if len(temperatures) != num_months:
    print("Data wrong")
else:
    # Calculate the annual average temperature
    average_temp = sum(temperatures) / len(temperatures)

    # Find the highest and lowest temperatures
    highest_temp = max(temperatures)
    lowest_temp = min(temperatures)

    # Print the results
    print("Data correct")
    print(f"Annual average temperature: {average_temp:.2f}°C")
    print(f"Highest temperature: {highest_temp}°C")
    print(f"Lowest temperature: {lowest_temp}°C")
