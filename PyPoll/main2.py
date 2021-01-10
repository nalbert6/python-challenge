# Modules
import os
import csv
import math


# Set path for file
csvpath = os.path.join("pypoll.csv")

#using csv module to read data
with open(csvpath, newline ='') as csvfile:
    #csv reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter = ',')

    header = next(csvreader)
    
    #variables
    khancount = 0
    khanpercent = 0.00
    correycount = 0
    correypercent = 0.00
    licount = 0
    lipercent = 0.00
    otooleycount = 0
    otooleypercent = 0.00
    winnercount = 0
    totalcount = 0
    winner = ""
    for row in csvreader:
        totalcount = totalcount + 1
        if(row[2] == "Khan"): # +1 vote for Khan
            khancount = khancount + 1
        elif (row[2] == "Correy"): # +1 vote for Correy
            correycount = correycount + 1
        elif (row[2] == "Li"): # +1 vote for Li
            licount = licount + 1
        elif (row[2] == "O'Tooley"): # +1 vote for O'Tooley
            otooleycount = otooleycount + 1
# percentage over the total
khanpercent = khancount / totalcount * 100
correypercent = correycount / totalcount * 100
lipercent = licount / totalcount * 100
otooleypercent = otooleycount / totalcount * 100
# type out the winner
winnercount = max(khancount, correycount, licount, otooleycount)
if(winnercount == khancount):
    winner = "Khan" 
elif(winnercount == correycount):
    winner = "Correy"
elif(winnercount == licount):
    winner = "Li"
else:
    winner = "O'Tooley"

#print totaly count
print (totalcount)


    # Store the file path associated with the file (note the backslash may be OS specific)
file = 'votes.txt'

# Open the file in "read" mode ('r') and store the contents in the variable "text"
with open(file, 'w') as text:

    # This stores a reference to a file stream
    print(text)
    formatTxt = (
        f"Election Results\n"
        f"---------------------------\n"
        f"Total votes: {str(totalcount)}\n"
        f"---------------------------\n"
        f"Khan: {str(khanpercent)} % "
        f"({str(khancount)})\n"
        f"Correy: {str(correypercent)} % "
        f"({str(correycount)})\n"
        f"Li: {str(lipercent)} % "
        f"({str(licount)})\n"
        f"O'Tooley: {str(otooleypercent)} % "
        f"({str(otooleycount)})\n"
        f"---------------------------\n"
        f"Winner: {str(winner)}"
        f"\n---------------------------\n"
    )
    # Invoke formatTxt
print(formatTxt)