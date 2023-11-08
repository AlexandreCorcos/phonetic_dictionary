import csv

# Open the file
with open('nato_phonetic_alphabet.csv', 'r') as file:
    # Read the file as a CSV
    reader = csv.reader(file)
    # Skip the header row
    next(reader)
    # Create a dictionary comprehension to store the letter-code pairs
    nato_dict = {row[0]: row[1] for row in reader}

# Print the dictionary
print(nato_dict)