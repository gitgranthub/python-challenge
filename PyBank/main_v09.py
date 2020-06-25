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
    csvreader = csv.reader(csvfile, delimiter=',')

    #remove header row
    csv_header = next(csvreader)
    
    for row in csv.reader(csvfile):
        count_of_months += 1
        total_sum += int(row[1])
        float_profit = float(row[1])
        total_profit_loss += float_profit
        

#moving average area for month to month average change

#data = [row for row in csvreader] #pulls data for iteration
data = (row[1]) #pulls data for iteration


month_profit = float(row[1]) #convert row value to float if needed
monthly_change_list = []

for i in range(len(data) - 1):
    months_row = data[i]
    months_date = months_row[0]
    months_profit = months_row[-1]
    last_months_row = data[i+1]
    last_months_profit = last_months_row[-1]

    monthly_return = (float(months_profit) - float(last_months_profit))#for percent change / last_months_profit
    monthly_change_list.append(monthly_return)
    #average_month_change = statistics.mean(monthly_change_list)
    average_month_change = sum(monthly_change_list) / float(len(monthly_change_list))


#     csvreader = csv.DictReader(infile)
#     data = {}
#     for row in reader:
#         for header, value in row.items():
#             try:
#     data[header].append(value)
#         except KeyError:
#     data[header] = [value]

# # extract the variables you want
# profit_loss_items = data['Profit/Losses']


# profit_loss_list = []
# window_size = 1

# i = 0
# moving_averages = []
# while i < len(profit_loss_list) - window_size + 1:
#     this_window = profit_loss_list[i : i + window_size]
# get current window

#     window_average = sum(this_window) / window_size
#     moving_averages.append(window_average)
#     i += 1

# moving_averages  

        
average_profit_loss = total_profit_loss / count_of_months

#add thousands comma seperator to total_sum
total_sum_comma = locale.format("%d", total_sum, grouping=True)

nl = "\n" #This variable allows 'next line' code to be embeded in this print statement f-string

print(f"{nl}{nl}Financial Analysis{nl}-------------------------------{nl}Total Months: {count_of_months}{nl}Total profit/loss: ${total_sum_comma}{nl}Average Change: {average_month_change}{nl}{nl}{nl}{nl}")

print(monthly_change_list)


