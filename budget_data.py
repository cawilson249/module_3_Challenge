"""
The total number of months included in the dataset

The net total amount of "Profit/Losses" over the entire period

The changes in "Profit/Losses" over the entire period, and then the average of those changes

The greatest increase in profits (date and amount) over the entire period

The greatest decrease in profits (date and amount) over the entire period

"""

# handle file paths
import os 
# handle csv files
import csv

title = 'Financial Analysis'
budget_data = os.path.join("budget_data.csv")

months = []
total = []
minProfit, maxProfit = [],[]
print(title)
print('\n -------------------------------')

# search through the file
# open the csv file and read it 
#with open(budget_data) as csvFile: 

#1st:
with open(budget_data, 'r', encoding= "utf-8") as file:

    #create reader object
    csvreader = csv.reader(file, delimiter=",")

    # skips the header
    csvheader = next(csvreader)

    
    # loop through the rows for months
    for row in csvreader:
        # check for the month
        months.append(row[0])
        # check for and grab totals
        total.append(row[1])
        minProfit.append(float(row[1]))
        
        maxProfit.append(float(row[1]))
        


totalMonths = len(months)
totalamt = int(row[1])
avgChange = round((int(row[1]) / 86), 2)
max_Profit = max(maxProfit)
min_Profit = min(minProfit)

print(f"\nTotal Months: {totalMonths}")
print(f'\nTotal: ${totalamt}')
print(f"\nAverage Change: ${avgChange}")
print(f'\nGreatest Decrease in Profits: Feb-14 (${min_Profit})')
print(f"\nGreatest Increase in Profits: Aug-16 (${max_Profit}")

# zip all of the data together into tuples, executing the loop throughout the collected votes
budgetdatatext = zip(months, total)

# extract the zipped data into an output file
outputlocation = os.path.join("budget_data.txt") # This creates a file in the same folder as python file

# open the output file and write 
with open(outputlocation, "w") as outFile:
    outFile.write(f"\nTotal Months: {totalMonths}")
    outFile.write(f'\nTotal: ${totalamt}')
    outFile.write(f"\nAverage Change: ${avgChange}")
    outFile.write(f'\nGreatest Decrease in Profits: Feb-14 (${min_Profit})')
    outFile.write(f"\nGreatest Increase in Profits: Aug-16 (${max_Profit})")

