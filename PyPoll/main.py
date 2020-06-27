import os
import csv

#reading in the relative path of the csv file to csvpath variable
csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #remove header row
    csv_header = next(csvreader)

    #variables holding values in the csv file
    khan_vote_total = 0
    correy_vote_total = 0
    li_vote_total = 0
    otooley_vote_total = 0
    total_votes = 0
    
    #iterate through csv file to pull values
    for row in csvreader:
        total_votes += 1
        
        if "Khan" in row:
            khan_vote_total += 1
        elif "Correy" in row:
            correy_vote_total += 1
        elif "Li" in row:
            li_vote_total += 1
        elif "O'Tooley" in row:
            otooley_vote_total += 1

#Final Statistical Analysis Calculations before print
canidates_totals_dict = {"Kahn": int(khan_vote_total), "Correy": int(correy_vote_total), "Li": int(li_vote_total), "O'Tooley": int(otooley_vote_total)}
khan_pct = round(khan_vote_total * 100.0 / total_votes)
correy_pct = round(correy_vote_total * 100.0 / total_votes)
li_pct = round(li_vote_total * 100.0 / total_votes)
otooley_pct = round(otooley_vote_total * 100.0 / total_votes)
winner = max(canidates_totals_dict, key=canidates_totals_dict.get) 


#This variable allows 'next line' code to be embeded in this print statement f-string
nl = "\n" 

#print to terminal
print(f"{nl}{nl}Election Results{nl}-------------------------------")
print(f"Total Votes: {total_votes}{nl}-------------------------------")
print(f"Kahn: {khan_pct}.000% ({khan_vote_total})")
print(f"Correy: {correy_pct}.000% ({correy_vote_total})")
print(f"Li: {li_pct}.000% ({li_vote_total})")
print(f"O'Tooley: {otooley_pct}.000% ({otooley_vote_total}){nl}-------------------------------")
print(f"Winner: {winner}{nl}-------------------------------")
print(f"{nl}{nl}")

#write to .txt file
results_file = os.path.join('analysis', 'analysis.txt')
with open(results_file, 'a') as analysis_write:
    analysis_write.write(f"{nl}{nl}Election Results{nl}-------------------------------{nl}")
    analysis_write.write(f"Total Votes: {total_votes}{nl}-------------------------------{nl}")
    analysis_write.write(f"Kahn: {khan_pct}.000% ({khan_vote_total}){nl}")
    analysis_write.write(f"Correy: {correy_pct}.000% ({correy_vote_total}){nl}")
    analysis_write.write(f"Li: {li_pct}.000% ({li_vote_total}){nl}")
    analysis_write.write(f"O'Tooley: {otooley_pct}.000% ({otooley_vote_total}){nl}-------------------------------{nl}")
    analysis_write.write(f"Winner: {winner}{nl}-------------------------------{nl}")
    analysis_write.write(f"{nl}{nl}")
