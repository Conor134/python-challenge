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
      # print(row)
      # print(count)

      if count == 0:
        PreviousValue = int(row[int(count)+1])
        print(PreviousValue, count)
      # print(count)
    
      # Value = int(row[1])
      # print(Value)
      # total = Value + total
      # print(total)
      # Diff = PreviousValue-Value
      # print(Diff)

      # TotalDiff = TotalDiff + Diff
     
      # average = total/count
      # AvgDiff = TotalDiff/count
      # print(Value,total,PreviousValue, Diff, average)

      if MaxDiff < Diff:
        MaxDiff = Diff
        MaxMonth = (row[int(count)+1])

    count = count +1
      # PreviousValue = Value

  



    # print("Financial Analysis")
    # print("____________________________")
    # print(f"The Sum of Profits is: ${int(total)}")
    
    # print(f"The total number of months:  {count}")

    # print(f"The average monthly profits is: ${int(average)}")