# Puzzle 2 Day 1
import os
import sys
# Variables
ris = 0
setFreq = set()



while True:
        # Open File
        fileOpen = open(os.path.expanduser("~/Desktop/puzzleInput.txt"))
        # Read File until EOF
        for line in fileOpen:
                if line.strip(): 
                        n = int(line)
                        ris=ris+n
                        # Checks ris in Set of frequency
                        if ris in setFreq:
                                print(ris)
                                sys.exit()
                        setFreq.add(ris)



            
            
           



