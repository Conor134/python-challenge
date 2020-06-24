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
     
    for row in csvreader:
        # index = int(row)
        # print(int(row))
        if count==0:
            previousValue = int(row[1])
            print("hello")
            print(row)
            

        print(count)
        print(GreatestIncrease)
        print(GreatestDecrease)

        Value = int(row[1])
        # print(Value)  
        # print(previousValue)    
        # print(row)    
            

        Value = int(row[1])
        total = Value + total
        # print(total)
        # print(Value)
        # print(previousValue)
        Diff = Value - previousValue 
        # print(Diff)
        totalDiff = totalDiff + Diff
        # print(totalDiff)

        
      
        # print(count)
        if count==1:
            GreatestIncrease = Diff
            GreatestDecrease = Diff
            


        if GreatestIncrease < Diff:
            GreatestIncrease = Diff
        if GreatestDecrease > Diff:
            GreatestDecrease = Diff

        count = count + 1
        previousValue=Value
    # print(total)
    # print(totalDiff)


# print(totalDiff)       
average = total/count
avgChange = round(float(totalDiff/(count-1)),2)
print(avgChange)


print("Financial Analysis")
print("____________________________")
    
print(f"The total number of months:  {count}")

print(f"The Sum of Profits is: ${int(total)}")

print(f"Average Change: ${avgChange}")
    
print(f"The Greatest Increase is:  {GreatestIncrease}")

print(f"The Greatest Decrease is:  {GreatestDecrease}")

print(f"The average monthly profits is: ${int(average)}")


    