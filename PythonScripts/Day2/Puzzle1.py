import os
import sys

#Variables
countTwo = 0
countThree = 0

checkSum = 1
mapCounts = {}
# Open File

# Read File until EOF
with open(os.path.expanduser("~/Desktop/AdventCode/input.txt")) as file:
    for line in file:
        mapCounts.clear()
        for i in range (len(line)):
            countTwo_local = 0
            countThree_local = 0
            key = line[i]
            value = mapCounts.get(key)
            
            if value == None:
                mapCounts[key]= 1
            else:
                mapCounts[key] = value + 1
        for c in mapCounts:
            
            if  mapCounts.get(c) == 2 and countTwo_local == 0:
                    print('aumento di 2')
                    countTwo = countTwo + 1
                    countTwo_local = countTwo_local + 1
            if  mapCounts.get(c) == 3 and countThree_local == 0 :
                    print('aumento di 3')
                    countThree = countThree + 1
                    countThree_local = countThree_local + 1
file.close()  
print(countThree, countTwo)              
checkSum = countThree * countTwo
print(checkSum)


                        
                                    

                        

                
