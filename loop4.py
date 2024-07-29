# Input two natural numbers from the user
max = int(input("Enter the max number: "))
den = int(input("Enter the den: "))


# Display all natural numbers up to and including max that are den by denominator
for number in range(1, max + 1):
    if number % den == 0:
        print(number)
