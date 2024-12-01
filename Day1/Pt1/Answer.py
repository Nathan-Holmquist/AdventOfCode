column1 = []
column2 = []

with open ("input.txt") as file:
    lines = file.readlines()
    for line in lines:
        data = line.split()
        column1.append(int(data[0]))
        column2.append(int(data[1]))


column1.sort()
column2.sort()

total_distance = 0
for i in range(len(column1)):
    if column1[i] > column2[i]:
        total_distance += column1[i] - column2[i]
    elif column1[i] < column2[i]:
        total_distance += column2[i] - column1[i]
    else:
        total_distance += 0

print("Total Distance:", total_distance)

