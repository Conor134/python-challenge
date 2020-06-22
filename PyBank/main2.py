# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# Set variable to check if we found the video
total = 0
count = 0

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

  OldValue = row([1,0])   
    for row in csvreader:
        total = float(row[1])+ total
        Value = int(row[1])
        Diff = Value - OldValue
        count = count +1
        average = total/count

  #  for x in range(count-1)



    print("Financial Analysis")
    print("____________________________")
    print(f"The Sum of Profits is: ${int(total)}")
    
    print(f"The total number of months:  {count}")

    print(f"The average monthly profits is: ${int(average)}")