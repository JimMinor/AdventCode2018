import os
import sys


# Read File until EOF
with open(os.path.expanduser("~/Desktop/input.txt")) as file:
    # Data Structures
    boxes = []
    for line in file:
        boxes.append(line)
    while((len(boxes)>1)):
        curr_box=(boxes.pop(0))
        for box in boxes:
            s = ""
            for i in range(0,(len(box))):
                if ( box[i] == curr_box[i]):
                    s = s + box[i]
                if((len(s))==(len(box))-1):
                    print(s)
                    file.close()
                    sys.exit(0)
    

file.close()    


