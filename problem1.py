import re

# Read the passage from a file (you can also hardcode the passage here)
with open('your_file.txt', 'r') as file:
    passage = file.read()

# Define a regular expression pattern to find 'the the' without 'a' in between
pattern = r'\bThe\s+The\b'

# Use re.findall to find all matches in the passage
matches = re.findall(pattern, passage, re.IGNORECASE)

# Count the number of matches
count = len(matches)

print(f"Number of 'the the' without 'a' in between: {count}")
