#Here I'm importing python librarys that allow me to
#read in csv files and allow me to have a file 'read'
#path that is OS independent.
import os
import csv

#variables holding values in the csv file
#total_months = []
#sum_profit_loss = 0
average_profit_loss = 0
greatest_increase = 0
greatest_decrease = 0

#reading in the relative path of the csv file to csvpath variable
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    #csv_reader = csv.reader(csvfile, delimiter=',')
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
    #Total months in col [0]
    #total_months = 0
    #for row in csv.reader(csvfile):
        #total_months += len(int(row[0])) #check this code**** My first attempt at counting months. I'm thinking the len funtion

    #Total Profit or Loss
    total_sum = 0
    for row in csv.reader(csvfile):
        total_sum += int(row[1])

total_months = 86 #for testing print, not produced from code above***     

nl = "\n" #This variable allows 'next line' code to be embeded in this print statement f-string

print(f"The total amount of months recorded is {total_months}.{nl}The company profit is ${total_sum}")