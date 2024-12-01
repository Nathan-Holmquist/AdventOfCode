column1 = []
column2 = []

with open ("input.txt") as file:
    lines = file.readlines()
    for line in lines:
        data = line.split()
        column1.append(int(data[0]))
        column2.append(int(data[1]))

similarityScore = 0
for i in range(len(column1)):
    similarityScore += (column2.count(column1[i]) * column1[i])

print("Similarity Score:", similarityScore)
