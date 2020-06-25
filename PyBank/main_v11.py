#******* CHANGING TO DictReader ***** TESTING

#Here I'm importing python librarys that allow me to
#read in csv files and allow me to have a file 'read'
#path that is OS independent.
import os
import csv
#I used this for comma seperated number for profit total. This would probably only be relative for the US.
import locale
locale.setlocale(locale.LC_ALL, 'en_US')
'en_US'
import statistics #adds another function list for averaging and such

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
    csvreader = csv.DictReader(csvfile, delimiter=',')

    #remove header row
    csv_header = next(csvreader)
    line_count = 0
    for row in csvreader:
        line_count += 1
        count_of_months += 1
        total_sum += sum(row["Date"])
        #float_profit = float(row[1])
        #total_profit_loss += float_profit
        

#moving average area for month to month average change
#     profit_loss_list = []
#     window_size = 1

#     for row in csv.reader(csvfile):
#         profit_loss_list.append(row[1])

#         i = 0
#         moving_averages = []
#         while i < len(profit_loss_list) - window_size + 1:
#             this_window = profit_loss_list[i : i + window_size]

#             window_average = sum(this_window) / window_size
#             moving_averages.append(window_average)
#             i += 1

# print(moving_averages)  

        
average_profit_loss = total_profit_loss / count_of_months

#add thousands comma seperator to total_sum
total_sum_comma = locale.format_string("%d", total_sum, grouping=True)

nl = "\n" #This variable allows 'next line' code to be embeded in this print statement f-string


print(f"{nl}{nl}Financial Analysis{nl}-------------------------------{nl}Total Months: {count_of_months}{nl}Total profit/loss: ${total_sum_comma}{nl}Average Change: {average_month_change}{nl}{nl}{nl}{nl}")

#print(profit_loss_list)


