input_raw = open("input.txt", "r")
input_string = (input_raw.read())

count = 0


    




def diskMap(input_string):
    output = ""
    count = 0
    times = 0
    for char in input_string:
        num = int(char)

        if (count%2 == 0):
            output += num*str(times)
            count+=1
            times += 1
        else:
            output += num*"."
            count+=1
            
        
    return output

def sort(fileBlocks):
    for char in fileBlocks:
        if char.isdigit() == True:
            for char in 
        



print(diskMap("12345"))





    
