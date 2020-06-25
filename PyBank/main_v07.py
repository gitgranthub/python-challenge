#Here I'm importing python librarys that allow me to
#read in csv files and allow me to have a file 'read'
#path that is OS independent.
import os
import csv
#I used this for comma seperated number for profit total. This would probably only be relative for the US.
import locale
locale.setlocale(locale.LC_ALL, 'en_US')
'en_US'

#variables holding values in the csv file
count_of_months = 0
total_sum = 0
total_profit_loss = 0
greatest_increase = 0
greatest_decrease = 0

#reading in the relative path of the csv file to csvpath variable
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    #csv_reader = csv.reader(csvfile, delimiter=',')
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    row_index_profit = 1
    for row in csv.reader(csvfile):
        count_of_months += 1
        total_sum += int(row[1])
        float_profit = float(row[row_index_profit])
        total_profit_loss += float_profit
        
average_profit_loss = total_profit_loss / total_sum
#add thousands comma seperator to total_sum
total_sum_comma = locale.format("%d", total_sum, grouping=True)

#total_months = 86 #for testing print, not produced from code above***     

nl = "\n" #This variable allows 'next line' code to be embeded in this print statement f-string

print(f"{nl}{nl}Financial Analysis{nl}-------------------------------{nl}Total Months: {count_of_months}{nl}Total profit/loss: ${total_sum_comma}{nl}Average Change: {average_profit_loss}{nl}{nl}{nl}{nl}")

