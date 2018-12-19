# Puzzle 1 Day 1
import os
import io
# Variables
ris = 0

# Open File
fileOpen = open(os.path.expanduser("~/Desktop/AdventCode/puzzleInput.txt"))
 # Read File until EOF
for line in fileOpen:
         if line.strip(): 
                n = int(line)
                ris=ris+n
print(ris)