import re


myInput = []
#todo adjust input 
with open("day3/input.txt") as f:
    for line in f:
        myInput.append(line)

pattern2 = "mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))"
pattern1 = "mul\((\d+),(\d+)\)"
total = 0



for myInputLine in myInput:
    #mySearched = re.findall(pattern1,myInputLine)
    mySearchedPre = re.findall(pattern2,myInputLine)
    
    enable = True
    mySearched = []
    for mul in mySearchedPre:


        if mul[2] == 'do()':
            enable = True
            breakpoint
        elif mul[3] == "don't()":
            enable = False
            breakpoint
        elif (enable):
            mySearched.append(mul)
        

    breakpoint


    for multInlist in mySearched:
        total += int(multInlist[0]) * int(multInlist[1])
        breakpoint

print(total)



breakpoint