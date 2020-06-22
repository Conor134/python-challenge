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
     
    for row in csvreader:
        print(row[1])
        # if row==2:
        #     Diff=0
        #     previousValue = int(row[1])
        #     print("hello")
            
        #     else:
        #     total = int( row[1]) + total:
        #     count = count +1
        #     Diff = int(row[1] - previousValue 
        #     totalDiff = totalDiff + Diff
    
        # if maxValue < int(row[1]):
        #     maxValue = int(row[1])
        # if minValue > int(row[1]):
        #     minValue = int(row[1])


       
    # average = total/count
    # avgChange = totDiff/(count-1)

    # print("Financial Analysis")
    # print("____________________________")
    
    # print(f"The total number of months:  {count}")

    # print(f"The Sum of Profits is: ${int(total)}")

    # print(f"Average Change: ${int(avgChange)}")
    
    # print(f"The Greatest Increase is:  {MaxValue}"

    # print(f"The Greatest Decrease is:  {MinValue}")

    # print(f"The average monthly profits is: ${int(average)}")


    