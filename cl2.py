# Initialize lists to store votes and counters
votes = []
vote_in_favor = 0
vote_against = 0
vote_abstained = 0

# Initialize variables to track specific vote information
first_favor_country = None
last_against_country = None

# Input the subject of the vote
subject = input("Enter the subject of the vote: ")

# Process votes from 44 countries
for i in range(1, 45):  # Countries numbered from 1 to 44
    while True:
        try:
            # Input the vote for the current country
            vote_input = input(
                f"Enter vote code for country No. {i} (1: in favor, 2: against, 3: abstained, 4: veto): ")

            # Convert the input to an integer
            vote_code = int(vote_input)

            # Check if the vote code is valid (1-4)
            if vote_code not in [1, 2, 3, 4]:
                print("Invalid vote code. Please enter a number between 1 and 4.")
                continue

            # Record the vote and update counters
            votes.append(vote_code)

            if vote_code == 1:
                vote_in_favor += 1
                if first_favor_country is None:
                    first_favor_country = i
            elif vote_code == 2:
                vote_against += 1
                last_against_country = i
            elif vote_code == 3:
                vote_abstained += 1
            elif vote_code == 4:
                print(f"Veto vote by country No. {i}. Exiting...")
                break  # Exit the loop if a veto is encountered

            # Exit the inner loop if the vote is valid
            break

        except ValueError:
            # Handle the case where input is not numeric
            print("Invalid input. Please enter a numeric value.")

    # Exit the outer loop if a veto is encountered
    if vote_code == 4:
        break

# Print the results
print(f"Votes in favor: {vote_in_favor}")
print(f"Votes against: {vote_against}")
print(f"Votes abstained: {vote_abstained}")

if first_favor_country is not None:
    print(f"First country that voted in favor: No. {first_favor_country}")
else:
    print("No country voted in favor.")

if last_against_country is not None:
    print(f"Last country that voted against: No. {last_against_country}")
else:
    print("No country voted against.")
