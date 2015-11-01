__author__ = 'Nick'

import csv
import pandas as pd

with open('wordSamples2.csv', 'r') as f:
    reader = csv.reader(f)
    your_list = list(reader)

listLen = len(your_list)
print(listLen)

run = False
newList = []

for x in your_list:
    if run == False:
        run = True
    else:
        i = 0
        while (i < int(x[2])):
            newList.append(x[1])
            i += 1

#print(newList)

newFrame = pd.DataFrame(newList)
newFrame[0].to_csv("output.csv", index_label="index")
