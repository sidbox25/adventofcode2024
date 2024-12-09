

base_array = []

def inCaseOfBreak(mylist,failCount,i):
    mylist.pop(i)
    failCount += 1
    i=0
    return mylist,failCount,i


#todo adjust input 
with open("day2/input.txt") as f:
    total = 0
    for line in f:
        currentReport = list(map(int,line.strip().split(" ")))
        isValid = True
        failCount = 0
        direction = "notDefined"
        adjustment = 0
        i = 0
        while i < len(currentReport)-1:
            
            if(failCount > 1):
                isValid=False
                break

            diff = abs(currentReport[i] - currentReport[i+1])
            if(diff < 1 or diff > 3):
                currentReport,failCount,i = inCaseOfBreak(currentReport,failCount,i)
                continue
                
            
            if(direction == "asc"):
                    if(currentReport[i] > currentReport[i+1]):
                        currentReport,failCount,i = inCaseOfBreak(currentReport,failCount,i)
                        continue   
            elif(direction == "desc"): 
                    if(currentReport[i] < currentReport[i+1]):
                        currentReport,failCount,i = inCaseOfBreak(currentReport,failCount,i)
                        continue
            elif(direction == "notDefined"):
                if(currentReport[i] - currentReport[i+1] < 0):
                    direction = "asc"
                else:
                    direction = "desc"
            i += 1

        if(isValid):
            total += 1
        
print(total)      







breakpoint
