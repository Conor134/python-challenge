# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# Set variables
total = 0
count = 0
Diff = 0
totalDiff =0
GreatestIncrease = 0
GreatestDecrease = 0

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first to skip when looping
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")


    # Loop through file to loop through data 
    for row in csvreader:
    # For the value on the first row, set it as the Previous Value so you can calculate differences
        if count==0:
            previousValue = int(row[1])
            
# Define the current value and calculate the running total 
        Value = int(row[1])
        total = Value + total

# Calculate the monthly difference 
        Diff = Value - previousValue 
        # Sum the total differences
        totalDiff = totalDiff + Diff
        
        # Get the first Difference Value between 1st and 2nd row
        if count==1:
            GreatestIncrease = Diff
            GreatestDecrease = Diff

        # See if the current value is greater/less than the previous values, then assign them
        if GreatestIncrease < Diff:
            GreatestIncrease = Diff
            # Set the month the match the Greatest Increase
            MaxMonth = row[0]
            
        if GreatestDecrease > Diff:
            GreatestDecrease = Diff
            # Set the month the match the Greatest Decrease
            MinMonth = row[0]

# set the previous value to the current value and adding to the count 
        count = count + 1
        previousValue=Value


    
# Calulate the average Monthly Change
average = total/count
avgChange = round(float(totalDiff/(count-1)),2)

# Print the results

print("Financial Analysis")
print("____________________________")
    
print(f"The total number of months:  {count}")

print(f"The Sum of Profits is: ${int(total)}")

print(f"Average Change: ${avgChange}")
    
print(f"The Greatest Increase is: {MaxMonth}:  (${GreatestIncrease})")

print(f"The Greatest Decrease is: {MinMonth}:  {GreatestDecrease}")


############################################
# Write reults to a file
############################################
# Specify the file to write to
output_path = os.path.join("Analysis", "Summary.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline="") as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(["Financial Analysis"])

    csvwriter.writerow(["____________________________"])
    
    csvwriter.writerow([f"The total number of months:  {count}"])

    csvwriter.writerow([f"The Sum of Profits is: ${int(total)}"])

    csvwriter.writerow([f"Average Change: ${avgChange}"])
    
    csvwriter.writerow([f"The Greatest Increase is: {MaxMonth}: (${GreatestIncrease})"])

    csvwriter.writerow([f"The Greatest Decrease is: {MinMonth}: (${GreatestDecrease})"])


