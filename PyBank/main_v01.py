#Here I'm importing python librarys that allow me to
#read in csv files and allow me to have a file read
#path OS independent.
import os
import csv

#reading in the relative path of the csv file to csvpath variable
csvpath = os.path.join('Resources', 'budget_data.csv')

#with open(csvpath) as csvfile:

with open(csvpath, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    
    for line in csvfile:
        print(line)



    
    #all_lines = list(csv.reader(csvfile, delimiter=','))
   

#print(all_lines)











