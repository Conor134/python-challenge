# Modules
import os
import csv


count = 0
FullList=[]
VoteCount = []
PercentVotes = []

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

# Open the CSV
with open(csvpath) as csvfile:
    PyPoll = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

    for row in PyPoll:
        # if count==0:
        #     Candidate = row[2]
        count += 1 
        Candidate = row[2]   
        # print(Candidate)
        FullList.append(Candidate)
     

# Make a copy of the Full List to Candidates
Candidates = set(FullList)
# Make Candidates have only the unique names by turning it into a list 
Candidates = list(Candidates)

# Get the number of unique Candidates
NumberCandidates = len(Candidates) 

# Set the values to be used in the next loop to zero
Percentage = 0
NumberVotes =  0
WinnerCount =0

#Loops through the unique candidates to count and make the relevant calcs for each unique candidate

for x in range(0,len(Candidates)):
    # Get the amount of votes for this unique candidate
    NumberVotes = FullList.count((Candidates[x]))
    # Calculate the percentage for this unique candiate
    Percentage = float(round((NumberVotes/count)*100,3))
    #Add the vote count and the percentage to their respective Lists while keeping the same order in the lists
    VoteCount.append(NumberVotes) 
    PercentVotes.append(Percentage)
    

# Calulate the Winner by looping through to get the max votes
for y in range(len(Candidates)):

   if WinnerCount < VoteCount[y]:
            Winner  = Candidates[y]
            # get the name with the same place in the VoteCount list
            WinnerCount= VoteCount[y]

# Printing the final results
print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(count))    
print("-------------------------")

# Looping through the Candidate list to output the corresponding Percent and Absolute votes for each candidate

for i in range(len(Candidates)):

    print(f"{Candidates[i]}:  {PercentVotes[i]:.3f}% ({VoteCount[i]})")

print("-------------------------")
print("The winner is: " + Winner)
print("-------------------------")


# Specify the file to write to
output_path = os.path.join("Analysis", "Summary.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline="") as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow(["Total Votes :" + str(count)])
    csvwriter.writerow(["-------------------------"])
    for i in range(len(Candidates)):
   
        csvwriter.writerow([f"{Candidates[i]}:  {PercentVotes[i]:.3f}% ({VoteCount[i]})"])

    csvwriter.writerow(["-------------------------"])
    
    csvwriter.writerow(["The winner is: " + Winner])