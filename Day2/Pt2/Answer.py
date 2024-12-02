safe = 0

def is_safe_sequence(numbers):
    increase_violations = sum(
        not (1 <= (numbers[i+1] - numbers[i]) <= 3) for i in range(len(numbers) - 1)
    )
    decrease_violations = sum(
        not (1 <= (numbers[i] - numbers[i+1]) <= 3) for i in range(len(numbers) - 1)
    )
    return increase_violations == 0 or decrease_violations == 0

with open("input.txt") as file:
    lines = file.readlines()  
    for line in lines: 
        numbers = list(map(int, line.split()))  

       
        if is_safe_sequence(numbers):
            safe += 1
            continue

        
        for i in range(len(numbers)):
            reduced_numbers = numbers[:i] + numbers[i+1:] 
            if is_safe_sequence(reduced_numbers):
                safe += 1
                break  

print("Safe sequences:", safe)
