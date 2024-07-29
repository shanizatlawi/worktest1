# Input two integers from the user
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Determine the smaller and larger number
start = min(num1, num2)
end = max(num1, num2)

# Display all integers between start and end (inclusive)
for number in range(start, end + 1):
    print(number)
