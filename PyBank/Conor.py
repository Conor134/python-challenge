# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# Set variable to check if we found the video
total = 0
count = 0
Diff = 0
totalDiff =0
GreatestIncrease = 0
GreatestDecrease = 0

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")


    # Loop through file to get data 
    for row in csvreader:
    # get the first value of to do the first calculation  
        if count==0:
            previousValue = int(row[1])
            # print("hello")
            # print(row)
            
    # After first row, continue through get the values
        # print(count)
        # print(GreatestIncrease)
        # print(GreatestDecrease)

         # print(Value)  
        # print(previousValue)    
        # print(row)    
            
# This is the current value, calculate the running total 
        Value = int(row[1])
        total = Value + total
        # print(total)
        # print(Value)
        # print(previousValue)
# Calculate the difference file
        Diff = Value - previousValue 
        # print(Diff)
        # Sum the total differences
        totalDiff = totalDiff + Diff
        # print(totalDiff)

        
      
        # Get the first Difference Value between 1st and 2nd row
        if count==1:
            GreatestIncrease = Diff
            GreatestDecrease = Diff
          

# See if the current value is greater/less than the previous vlaues 
        if GreatestIncrease < Diff:
            GreatestIncrease = Diff
        if GreatestDecrease > Diff:
            GreatestDecrease = Diff
# set the previous value to the current value before adding to the count 
        count = count + 1
        previousValue=Value
    # print(total)
    # print(totalDiff)


# print(totalDiff)       
# Calulate the average Month value, Avg Monthly Change
average = total/count
avgChange = round(float(totalDiff/(count-1)),2)
print(avgChange)


print("Financial Analysis")
print("____________________________")
    
print(f"The total number of months:  {count}")

print(f"The Sum of Profits is: ${int(total)}")

print(f"Average Change: ${avgChange}")
    
print(f"The Greatest Increase is:  (${GreatestIncrease})")

print(f"The Greatest Decrease is:  {GreatestDecrease}")

print(f"The average monthly profits is: ${int(average)}")
