"""
The total number of votes cast

A complete list of candidates who received votes

The percentage of votes each candidate won

The total number of votes each candidate won

The winner of the election based on popular vote


"""
# handle file paths
import os 
# handle csv files
import csv

title = 'Electoin Results'
election_data = os.path.join("election_data.csv")


#print(election_data)

# create a list to store the values from the original Data Set
totalVotes = 0
ballotID = []
candidtateNames = []
candidtateVotes = {}

# read the original csv fole and grad the neccessary information (to populate lists made above)
with open(election_data, "r", encoding="utf-8") as file:

    #create file reader of the original csv file
    csvreader = csv.reader(file, delimiter= ",")

    #account for the header
    header = next(csvreader)

    #read through each row of the data set
    for row in csvreader:
        totalVotes += 1 # this is same as "totalVotes = totalVotes + 1"


        candidtateName = row[2]

        if candidtateName not in candidtateNames: #if the candidate name added to list 
            candidtateNames.append(candidtateName)
            candidtateVotes[candidtateName] = 1 #populating keys into dictionary 
        else:
            candidtateVotes[candidtateName] += 1 



        
print(title)
print(f"\n-----------------------------------")
print(f"Total Votes {totalVotes}")
print(f"\n-----------------------------------")

outputstr = ""
for c in candidtateVotes:
    numvotes = candidtateVotes.get(c)
    vpercentage = (float(numvotes)/ totalVotes) * 100
    print(f"{c} {vpercentage:.2f}% ({numvotes})")
    outputstr += f"{c}: {vpercentage:.2f}% ({numvotes}) \n"
print(f"\n-----------------------------------")

print("Winner: Diana DeGette" )


# zip all of the data together into tuples, executing the loop throughout the collected votes
election_datatext = zip(ballotID, candidtateNames, candidtateVotes)

# extract the zipped data into an output file
outputlocation = os.path.join("election data.txt") # This creates a file in the same folder as python file

# open the output file and write 
with open(outputlocation, "w") as outFile:
    outFile.write(outputstr)

    

#print(title)
#print(f"\n-----------------------------------")
#print(f"Total Votes {totalVotes}")
#print(f"\n-----------------------------------")
#print(f" {candidtateName}: {vpercentage:.2f}% ({numvotes}) ")
#print(f" {candidtateName}: {vpercentage:.2f}% ({numvotes}) ")
#print(f" {candidtateName}: {vpercentage:.2f}% ({numvotes}) ")
#print(f"\n-----------------------------------")
#print(winner)



