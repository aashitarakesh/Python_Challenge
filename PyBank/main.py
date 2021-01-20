# Create a Python script that analyzes the records to calculate each of the following:

#   * The total number of months included in the dataset

#   * The net total amount of "Profit/Losses" over the entire period

#   * Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

#   * The greatest increase in profits (date and amount) over the entire period

#   * The greatest decrease in losses (date and amount) over the entire period


# Import Modules
import os
import csv

# Set up Variables
months = []
monthly_profit_change = []
month_count = 0
amount_profit = 0
amount_loss = 0
net_total = 0
current_month_profit_loss = 0
previous_month_profit_loss = 0

# Set path for budget_data
csvpath = os.path.join("Resources", "budget_data.csv")

# Open csv File 

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip Headers
    next(csvreader)

    # Count Total number of months 
    for row in csvreader:
        month_count += 1

        #Calculate Net Total Profit/Loss
        current_month_profit_loss = int(row[1])
        net_total += current_month_profit_loss
        
        # Calculate Monthly change in profits       
        if (month_count == 1):

       # Make the value of previous month to be equal to current month            
            previous_month_profit_loss = current_month_profit_loss
            continue
        else:

            # Compute change in profit loss 
            monthly_profit_change.append(current_month_profit_loss - previous_month_profit_loss)
        
            # Append each month to the months[]         
            months.append(row[0])       

            # Adjust the previous month P/L to be equal to current month P/L        
            previous_month_profit_loss = current_month_profit_loss
         
    # Calculate Average Change in "Profit/Losses" over the entire period
    total_profit_loss = sum(monthly_profit_change)
    average_profit_loss = round(total_profit_loss/(month_count - 1), 2)

    # Greatest Increase/Decrease in profits
    greatest_increase_profit = max(monthly_profit_change)
    greatest_decrease_profit = min(monthly_profit_change)

    # Determine Index values of Greatest Increase/Decrease in profits
    greatest_increase_month = months[monthly_profit_change.index(greatest_increase_profit)]
    greatest_decrease_month = months[monthly_profit_change.index(greatest_decrease_profit)]

    # Print Analysis to Terminal
    print("Financial Analysis")
    print("-------------------------------------")
    print(f'Total Months : {month_count}')
    print(f'Net Total : ${net_total}')
    print(f'Average Change : ${average_profit_loss}')
    print(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_profit})')
    print(f'Greatest decrease in Profits: {greatest_decrease_month} (${greatest_decrease_profit})')

# Specify the file to write to 
output_path = os.path.join("Analysis", "Financial_Analysis.txt")

# Export a txt file with Financial Analysis
with open(output_path, 'w') as txtfile:
    
    txtfile.write("Financial Analysis\n")   
    txtfile.write("-------------------------------------\n")
    txtfile.write(f'Total Months : {month_count}\n')
    txtfile.write(f'Net Total : ${net_total}\n')
    txtfile.write(f'Average Change : ${average_profit_loss}\n')
    txtfile.write(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_profit})\n')
    txtfile.write(f'Greatest decrease in Profits: {greatest_decrease_month} (${greatest_decrease_profit})\n')
