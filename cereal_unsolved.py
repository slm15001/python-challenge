import os
import csv

# Set path for file
csvpath = os.path.join("C:/Users/Sal/Desktop/0728class", "cereal.csv")


# Open the CSV
with open("C:/Users/Sal/Desktop/0728class/cereal.csv", "rt") as csvfile:
    csvreader = csv.reader(csvfile)
    i = next(csvreader)
    
print(i)


