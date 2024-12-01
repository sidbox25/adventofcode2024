
#todo adjust input 
array_left = []
array_right = []



with open("day1/input.txt") as f:
    total = 0
    for line in f:

        array_left.append(int(line.strip().split("   ")[0]))
        array_right.append(int(line.strip().split("   ")[1]))


#part 1

"""
array_left.sort()
array_right.sort()

total = 0

for i in range(len(array_left)):
    diff = abs(array_left[i] - array_right[i])
    total += diff

print(total) 
"""

#part 2

total = 0
for i in range(len(array_left)):
    similarity = len(list(filter(lambda x: x==array_left[i],array_right)))
    total += array_left[i]*similarity
    
print(total)




    

