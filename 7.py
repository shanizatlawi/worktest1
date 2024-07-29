# Input a two-digit number from the user
number = int(input("Enter a two-digit number: "))

# Extract the tens and units digits
tens = number // 10
units = number % 10

# Calculate the sum of the digits
sum_of_digits = tens + units
if len(number) > 2:
    print('error, number has more than four degrees')
else:# Print the sum of the digits
 print("The sum of the digits of", number, "is:", sum_of_digits)
