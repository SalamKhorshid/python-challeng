# Importing required modules:
import os
import csv

# Open CSV file:
with open ('/Users/salam/Documents/BootCamp/Weekly Challenges/python-challenge/PyBank/Resources/budget_data.csv','r') as budget_data:
    lines = csv.reader(budget_data)

    # Skip the header:
    header = next(lines)
    
    # initialize variables:
    months = 0
    total = 0
    items = []
    changes=[]
    dates = []

    # Iterate over each row in the CSV:
    previous_profit_loss = None
    for line in lines:
        
        # The total number of months:
        months = months + 1

        # The net total amount of the entire period:
        total = total + int(line[1])

        # Calculate the profit/losses changes:
        if previous_profit_loss is not None:
            change = int(line[1]) - previous_profit_loss
            changes.append(change)
            dates.append(line[0])

        previous_profit_loss = int(line[1])

    # The average of the profit/losses changes:
    average_change = sum(changes) / len(changes)

    # Round the average change to the nearest two decimals:
    round_average_change = round(average_change,2)

    print('Total Months: ' + str(months))
    print('Total: $' + str(total))
    print('Average Change: $' + str(round_average_change))
    
    # Find greatest profit and loss:
    greatest_profit = max(changes)
    greatest_loss = min (changes)

    # Find the dates of the greatest profit and loss:
    greatest_profit_index = changes.index(greatest_profit)
    greatest_loss_index = changes.index(greatest_loss)
    date_greatest_profit = dates[greatest_profit_index]
    date_greatest_loss = dates [greatest_loss_index]

    print ('Greatest Increase in profits: ' + str(date_greatest_profit) + ' ($)' + str(greatest_profit) + ')')
    print ('Greatest Decrease in Profits: ' + str(date_greatest_loss) + ' ($)' + str(greatest_loss) + ')')

# Create a new text file:
analysis = '/Users/salam/Documents/BootCamp/Weekly Challenges/python-challenge/PyBank/analysis'
output = os.path.join(analysis, 'PyBank_Text.txt')

# Open the new text file and export the results to it:
with open (output, 'w') as file:
    file.write('Total Months: ' + str(months) + '\n')
    file.write('Total: $' + str(total) +'\n')
    file.write('Average Change: $' + str(round_average_change) + '\n')
    file.write('Greatest Increase in profits: ' + str(date_greatest_profit) + ' ($)' + str(greatest_profit) + ')' + '\n')
    file.write('Greatest Decrease in Profits: ' + str(date_greatest_loss) + ' ($)' + str(greatest_loss) + ')' + '\n')
