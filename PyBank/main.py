
import os
import csv
#I used this for comma seperated number for profit total. This would probably only be relative for the US.
import locale
locale.setlocale(locale.LC_ALL, 'en_US')
'en_US'
#reading in the relative path of the csv file to csvpath variable
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #remove header row
    csv_header = next(csvreader)

    #variables holding values in the csv file
    count_of_months = 0
    total_revenue = 0
    this_month_revenue = 0
    last_month_revenue = 0
    revenue_change = 0
    revenue_changes = []
    months = []
    
    for row in csvreader:
        count_of_months += 1
        this_month_revenue = float(row[1])
        total_revenue += this_month_revenue
        months.append(row[0])
        if count_of_months > 1:
            revenue_change = this_month_revenue - last_month_revenue
            revenue_changes.append(revenue_change)
        last_month_revenue = this_month_revenue

#Final Statistical Analysis Calculations before print
sum_rev_changes = sum(revenue_changes)
average_change = sum_rev_changes / (count_of_months - 1)
max_change = max(revenue_changes)
min_change = min(revenue_changes)
max_month_index = revenue_changes.index(max_change)
min_month_index = revenue_changes.index(min_change)
max_month = months[max_month_index + 1]
min_month = months[min_month_index + 1]

#round the decimals
total_revenue = int(total_revenue)
average_change = int(average_change)
max_change = int(max_change)
min_change = int(min_change)

#add thousands comma seperator to total_sum
total_sum_comma = locale.format_string("%d", total_revenue, grouping=True)
average_month_change_comma = locale.format_string("%d", average_change, grouping=True)
max_change_comma = locale.format_string("%d", max_change, grouping=True)
min_change_comma = locale.format_string("%d", min_change, grouping=True)
nl = "\n" #This variable allows 'next line' code to be embeded in this print statement f-string


print(f"{nl}{nl}Financial Analysis{nl}-------------------------------")
print(f"Total Months: {count_of_months}{nl}Total: ${total_sum_comma}")
print(f"Average Change: ${average_month_change_comma}")
print(f"Greatest Increase in Profits: {max_month} ${max_change_comma} USD")
print(f"Greatest Decrease in Profits: {min_month} ${min_change_comma} USD")
print(f"{nl}{nl}")
