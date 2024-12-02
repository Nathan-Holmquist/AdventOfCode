safe = 0

with open("input.txt") as file:
    lines = file.readlines()  
    for line in lines: 
        numbers = list(map(int, line.split()))  
        is_increasing = all(1 <= (numbers[i+1] - numbers[i]) <= 3 for i in range(len(numbers) - 1))
        is_decreasing = all(1 <= (numbers[i] - numbers[i+1]) <= 3 for i in range(len(numbers) - 1))
    
        if is_increasing or is_decreasing:
            safe += 1
print("Safe numbers:", safe)




        





