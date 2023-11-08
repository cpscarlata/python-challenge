import csv
import os
# Set file path
csvpath = os.path.join(r'C:\Users\cpsca\OneDrive\Documents\Python Scripts\PyBank\Resources','budget_data.csv')

# Declare Variables
total_months = 0
net_total = 0
previous_profit_loss = 0
profit_losses_changes = []
months = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

# Total Months & Profit/Losses

# Open the CSV file for reading
with open(csvpath, 'r') as csvfile:
    # Create a CSV reader object
    csv_reader = csv.reader(csvfile)

    header = next(csv_reader)

    for row in csv_reader:
        # Count the number of total months
        total_months += 1

        # Calculate the net total profit/loss
        net_total += int(row[1])
      
        # Calculate the change in profit/loss from the previous month
        current_profit_loss = int(row[1])
        change = current_profit_loss - previous_profit_loss
        profit_losses_changes.append(change)
        months.append(row[0])

        # Find the greatest increase and decrease in profits
        if change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = change
        if change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = change

        # Update the previous profit/loss for the next iteration
        previous_profit_loss = current_profit_loss

        average_change = sum(profit_losses_changes) / len(profit_losses_changes)

        print("Financial Analysis")
        print("---------------------------")
        print(f"Total Months: {total_months}")
        print(f"Total: ${net_total}")
        print(f"Average Change: ${average_change:.2f}")
        print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
        print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")
