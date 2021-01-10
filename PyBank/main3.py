# Modules
import os
import csv
import math


# Set path for file
csvpath = os.path.join("budget_data.csv")

#using csv module to read data
with open(csvpath, newline ='') as csvfile:
    #csv reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    print("Analyzing")
    print("---------------------------")
    
    #Counter for the total of the months
    #This code works
    header = next(csvreader)
    
    #variables
    count = 0
    total = 0
    average = 0
    current = 0
    highProfit = 0
    highLoss = 0
    ProfitLossdate = ""
    Lossdate = ""
    for row in csvreader:
        total += int(row[1])
        count += 1
        current = int(row[1])
        if(current >= 0): # decide if profit or loss
            if(current > highProfit): #store highest profit date
                highProfit = current
                Profitdate = str(row[0])
        elif(current < 0):
            if(current < highLoss): #store worst loss ever
                highLoss = current
                Lossdate = str(row[0])
average = total / count #average profit over x months
print (total)


    # Store the file path associated with the file (note the backslash may be OS specific)
file = 'input.txt'

# Open the file in "read" mode ('r') and store the contents in the variable "text"
with open(file, 'w') as text:

    # This stores a reference to a file stream
    print(text)
    formatTxt = (
        f"Financial Analysis\n"
        f"---------------------------\n"
        f"Total months: {str(count)}\n"
        f"Total: $ {str(total)}\n"
        f"Greatest Increase In Profits: {str(Profitdate)}"
        f"($ {str(highProfit)})\n"
        f"Greatest Decrease In Profits: {str(Lossdate)}"
        f"($ {str(highLoss)})\n" 
    )
    # Invoke formatTxt
print(formatTxt)