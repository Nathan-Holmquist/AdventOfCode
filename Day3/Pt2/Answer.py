import re

# Read the corrupted memory
with open("input.txt") as file:
    corrupted_memory = file.read()

# Patterns for mul(X,Y), do(), and don't()
mul_pattern = r"mul\((\d+),(\d+)\)"
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"

# Combine all patterns into a single regex
combined_pattern = f"{do_pattern}|{dont_pattern}|{mul_pattern}"

# Find all matches (in order of appearance)
matches = re.finditer(combined_pattern, corrupted_memory)

# Initialize state
mul_enabled = True
total_sum = 0

# Process matches
for match in matches:
    if match.group(0).startswith("do()"):
        mul_enabled = True  # Enable mul instructions
    elif match.group(0).startswith("don't()"):
        mul_enabled = False  # Disable mul instructions
    else:
        # Match a mul(X,Y) instruction
        if mul_enabled:
            x, y = map(int, match.groups())
            total_sum += x * y

print("Final Result:", total_sum)
