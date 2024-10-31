# Import necessary modules
import csv
import os

# establish paths of files to load and output
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to hold the total number of months and the total changes in profit/loss
total_months = 0
total_net = 0

# Add more variables and lists to track other necessary financial data
change = 0 #stores the difference between current and previous row as a variable
changeList = [] #creates changes as list that can store changes
greatestIncrease = ["",0] #stores the greatest increase in Profit/Loss as a list, with a string for the month and a number for the value
greatestDecrease = ["",999999] #stores the greatest decrease in Profit/Loss as a list, with a string for the month and a number for the value
averageChange = 0 #stores the average change between months in Profit/Loss 

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
    previous_net = float(firstRow[1]) #initializing previous net change as the Profit/Loss value at the first row of the file (will be used in the first loop)

    # Process each row of data in a for loop
    for row in reader:
        # Track the total
        total_months += 1 #adds 1 to total month count
        total_net += int(row[1]) #profit/loss is stored in column B, which is index 1

        # Track the net change in profit/loss by subtracting the profit/loss of the previous row from the profit/loss of the current row
        change = float(row[1]) - previous_net
        previous_net = float(row[1]) #save the profit/loss of the current row as the new previous_net, to be used in the next loop (where the current row becomes the previous row)
        changeList.append(change) #add the calculated change to the list of changes

        #Calculate the greatest increase between months (maximum change) (month and amount)
        if change > float(greatestIncrease[1]): #compared current change to stored greatestIncrease. If current change is greater,
            greatestIncrease[0] = row[0] #save current month as the greatestIncrease month
            greatestIncrease[1] = int(change) #save current change as the greatestIncrease change

        #Calculate the greatest decrease between months (minimum change) (month and amount)
        if change < float(greatestDecrease[1]): #compared current change to stored greatestDecrease. If current change is less,
            greatestDecrease[0] = row[0] #save current month as the greatestDecrease month
            greatestDecrease[1] = int(change) #save current change as the greatestDecrease change

# Calculate the average net change across the months
    changeCount = len(changeList) #determine the number of changes using len()
    changeTotal = 0 #initialize running total
    #use a loop to loop through each change in the list
    for c in changeList:
        #add the change to the running total
        changeTotal += c
#calculate average change by dividing changeTotal (the running total) by changeCount (the number of changes), round up to 2 decimal places
averageChange = round(changeTotal/changeCount,2)

# Generate the output summary
output = (f"Financial Analysis\n\n"
          "------------------------\n\n"
          f"Total Months: {total_months}\n\n" #print the total number of months
          f"Total: ${total_net}\n\n" #print the total $ value
          f"Average Change:${averageChange}\n\n" #print the average change
          f"Greatest Increase in Profits: {greatestIncrease[0]} $({greatestIncrease[1]})\n\n" #print the month and value of the greatest increase
          f"Greatest Decrease in Profits: {greatestDecrease[0]} $({greatestDecrease[1]})") #print the month and value of the greatest decrease

# Print the output to the terminal
print(output)
# Write the results to a text file
with open(file_to_output, "w") as txt_file:
     txt_file.write(output)
