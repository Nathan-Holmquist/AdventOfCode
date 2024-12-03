# Def looked this one up
import re

with open("input.txt") as file:
    corrupted_memory = file.read()



pattern = r"mul\((\d+),(\d+)\)"



matches = re.findall(pattern, corrupted_memory)


total_sum = 0
for match in matches:
    x, y = map(int, match)  
    total_sum += x * y      


print("Final Result:", total_sum)
