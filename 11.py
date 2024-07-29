# Input age and height from the user
age = int(input("Enter age: "))
height = int(input("Enter height in cm: "))

# Determine if the person is allowed to board the roller coaster
if (8 <= age <= 18 and height > 115) or (age > 18 and height > 100):
    print("Allowed to enter the facility.")
else:
    print("Not allowed to enter the facility.")
