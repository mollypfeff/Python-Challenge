
# Dependencies
import csv
import os
# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path
# Define variables to track the financial data
total_months = 0
total_net = 0

# Add more variables to track other necessary financial data
change = 0 #stores the difference between current and previous row as a variable
changeList = [] #creates changes as list that can store changes
greatestIncrease = ["",0]
greatestDecrease = ["",999999]
averageChange = 0
# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)
    # Skip the header row
    header = next(reader)
    # Extract first row to avoid appending to net_change_list
    firstRow = next(reader)
    # Track the total and net change
    total_months +=1 #establishing the month count at row 1 as '1'
    
    total_net += int(firstRow[1]) #profit/loss is stored in column B, which is index 1
    previous_net = float(firstRow[1])
    # Process each row of data
    for row in reader:
        # Track the total
        total_months += 1 #adds 1 to total month count
        total_net += int(row[1]) #profit/loss is stored in column B, which is index 1
        # Track the net change
        change = float(row[1]) - previous_net
        previous_net = float(row[1])
        changeList.append(change)
        #Calculate the greatest increase between months (maximum change) (month and amount)
        if change > float(greatestIncrease[1]):
            greatestIncrease[0] = row[0]
            greatestIncrease[1] = int(change)
        #Calculate the greatest decrease between months (minimum change) (month and amount)
        if change < float(greatestDecrease[1]):
            greatestDecrease[0] = row[0]
            greatestDecrease[1] = int(change)
# Calculate the average net change across the months
    changeCount = len(changeList)
    changeTotal = 0 #initialize running total
    #use a loop to loop through the numbers in the list
    #wouldn't use a list condition bc the output's just a value, not a new list
    for c in changeList:
        #add the number to the running total
        changeTotal += c
#calculate average change by dividing changeTotal by changeCount, round up to 2 decimal places
averageChange = round(changeTotal/changeCount,2)
# Generate the output summary
output = (f"Financial Analysis\n\n"
          "------------------------\n\n"
          f"Total Months: {total_months}\n\n"
          f"Total: ${total_net}\n\n"
          f"Average Change:${averageChange}\n\n"
          f"Greatest Increase in Profits: {greatestIncrease[0]} $({greatestIncrease[1]})\n\n"
          f"Greatest Decrease in Profits: {greatestDecrease[0]} $({greatestDecrease[1]})")
# Print the output
print(output)
# Write the results to a text file
with open(file_to_output, "w") as txt_file:
     txt_file.write(output)
