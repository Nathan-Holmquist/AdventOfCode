
lines = open("input.txt", "r").readlines()

grid = []
print(grid)
for line in lines:
    grid.append([ch for ch in line if ch != "\n"])

    # grid[r-1][c-1]

count = 0
for r, row in enumerate(grid):
    for c, column in enumerate(row):
        if column != "X":
            continue
        if "".join(row[c:c+4]) == "XMAS":
            print("Found right")
            count+=1
        if "".join(row[c-4:c]) == "SAMX":
            print("Found left")
            count+=1
        if r+3 < len(grid) and grid[r+1][c] == "M" and grid[r+2][c] == "A" and grid[r+3][c] == "S":
            print("Found down")
            count+=1
        if r-3 >=0 and grid[r-1][c] == "M" and grid[r-2][c] == "A" and grid[r-3][c] == "S":
            print("Found up")
            count+=1
        if r-3 >= 0 and c-3 >=0 and grid[r-1][c-1] == "M" and grid[r-2][c-2] == "A" and grid[r-3][c-3] == "S":
            print("Found ne")
            count+=1
        if r+3 < len(grid) and c+3 < len(grid[0]) and grid[r+1][c+1] == "M" and grid[r+2][c+2] == "A" and grid[r+3][c+3] == "S":
            print("Found se")
            count+=1    
        if r+3 < len(grid) and c-3 >=0 and grid[r+1][c-1] == "M" and grid[r+2][c-2] == "A" and grid[r+3][c-3] == "S":
            print("Found sw")
            count+=1
        if r-3 >= 0 and c+3 < len(grid[0]) and grid[r-1][c+1] == "M" and grid[r-2][c+2] == "A" and grid[r-3][c+3] == "S":
            print("Found ne")
            count+=1 



print(count)