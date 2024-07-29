# input the 4-digit number from the user (assuming it's entered as a string for simplicity)
number_str = input("Enter a 4-digit number:")

# extract the rightmost digit
rightmost_digit = number_str[-1]
if len(number_str) > 4:
    print('error, number has more than four degrees')
else:
    print("the rightmost digit of the number is:", rightmost_digit)


