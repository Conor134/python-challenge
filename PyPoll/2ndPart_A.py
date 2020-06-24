# Modules
import os
import csv
my_list = []

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

  

    for row in csvreader:
        my_list.append(row[2])
    print(len(my_list))
    candidates=set(my_list)
    print(len(candidates))
    print(candidates)


    # unique = [used.append(x) for x in csvreader if x not in used]
    # print (used)
    # print(unique)

    

# The simplest is to convert to a set then back to a list:

# my_list = list(set(my_list))
# print(len(my_list))
# print(my_list)

#   my_list = ()

#     capital_letters = [letter.upper() for letter in csvreader]
