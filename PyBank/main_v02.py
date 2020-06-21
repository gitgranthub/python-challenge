#Here I'm importing python librarys that allow me to
#read in csv files and allow me to have a file 'read'
#path that is OS independent.
import os
import csv

#variables holding values in the csv file
total_months = []
sum_profit_loss = 0
average_profit_loss = 0
greatest_increase = 0
greatest_decrease = 0

#reading in the relative path of the csv file to csvpath variable
csvpath = os.path.join('Resources', 'budget_data.csv')

#with open(csvpath) as csvfile:

with open(csvpath, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    
    for line in csvfile:
        print(line)



    
    #all_lines = list(csv.reader(csvfile, delimiter=','))
   

#print(all_lines)











