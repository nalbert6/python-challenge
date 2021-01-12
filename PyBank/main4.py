# import dependecies 
import os
import csv

# file path
filepath = os.path.join('budget_data.csv')

# track various financial parameters
total_months = 0 
months = []
change = []
greatest_increase = ["", 0] #whatever empty value should be more than zero
greatest_decrease =["", 999999999]
total_net = 0

with open (filepath) as financial_data:
    csvreader = csv.reader(financial_data)

    #read header
    header = next(csvreader)

    #extract first row to avoid appending change
    first_row = next(csvreader)
    total_months += 1
    total_net += int(first_row[1]) #first_row as total_net
    prev_net = int(first_row[1]) # whatever value in index 1 

    # start for loop
    for row in csvreader: 
        total_months += 1
        total_net += int(row[1])
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        change += [change]
        months += [row[0]] 

        #calculate greatest increase and greatest decrease value
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change   

        #calculate average net change
    monthly_average = sum(change)/ len(change)

        # output
 output(
		f"Financial Analysis\n"
        f"---------------------------\n"
        f"Total months: {str(total_months)}\n"
        f"Total: $ {str(total_net)}\n"
        f"Average Change: {str(monthly_average)}"
        f"Greatest Increase In Profits: {greatest_increase[0]}(${greatest_increase[1]})\n"
        f"Greatest Decrease In Profits: {greatest_decrease[0]}(${greatest_decrease[1]})\n"
		)
   
 print(output)
 
 txt_file.write(output)
