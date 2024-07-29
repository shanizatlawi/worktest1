number_str = input("Enter a 4-digit number:")

# extract the rightmost digit
right2_digit = number_str[-2]
if len(number_str) > 4:
    print('error, number has more than four degrees')
else:
    print("the righ2 digit of the number is:", right2_digit)
