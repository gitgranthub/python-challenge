
#Here I'm importing python librarys that allow me to
#read in csv files and allow me to have a file 'read'
#path that is OS independent.
import os
import csv
#I used this for comma seperated number for profit total. This would probably only be relative for the US.
import locale
locale.setlocale(locale.LC_ALL, 'en_US')
'en_US'

#made a avg funtion to help get the average of a list
def avg(x):
    total = 0
    for i in x:
        total = total + i
        defavg = total / len(x)
    return defavg

#variables holding values in the csv file
count_of_months = 0
total_sum = 0
total_profit_loss = 0

greatest_increase = 0
greatest_decrease = 0
plist = []

#reading in the relative path of the csv file to csvpath variable
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')

    #remove header row
    csv_header = next(csvreader)
    
 
    for row in csvreader:
        count_of_months += 1
        total_sum += int(row[1])
        float_profit = float(row[1])
        total_profit_loss += float_profit
        plist.append(row[1])

    #convert profit/loss list into float before calculating Average Change
    list_float = [float(i) for i in plist]
    m_to_m_average = []
    
    #Loop for calculating Average Change (moving average / 1 month wwindow)
    for i in list_float:
        m_to_m = i + i
        m_to_m_sum = m_to_m / 2
        m_to_m_average.append(m_to_m_sum)



#Final Statistical Analysis Calculations before print

average_month_change = avg(m_to_m_average) / len(m_to_m_average)     
average_profit_loss = total_profit_loss / count_of_months

#add thousands comma seperator to total_sum
total_sum_comma = locale.format_string("%d", total_sum, grouping=True)
average_month_change_comma = locale.format_string("%d", average_month_change, grouping=True)
nl = "\n" #This variable allows 'next line' code to be embeded in this print statement f-string


print(f"{nl}{nl}Financial Analysis{nl}-------------------------------{nl}Total Months: {count_of_months}{nl}Total profit/loss: ${total_sum_comma}{nl}Average Change: ${average_month_change_comma}{nl}{nl}{nl}{nl}")



