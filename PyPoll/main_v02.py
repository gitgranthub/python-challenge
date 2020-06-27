import os
import csv

#a function to get the percentage of each canidates votes
def get_letter_percentage(dictionary, s):
    sum = 0
    for key in dictionary:
        sum += dictionary[key]

    return round(int(dictionary[s])) / round(int(sum))

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
khan_pct = get_letter_percentage(canidates_totals_dict, "Kahn")
correy_pct = get_letter_percentage(canidates_totals_dict, "Correy")
li_pct = get_letter_percentage(canidates_totals_dict, "Li")
otooley_pct = get_letter_percentage(canidates_totals_dict, "O'Tooley")
winner = max(canidates_totals_dict, key=canidates_totals_dict.get) 


#This variable allows 'next line' code to be embeded in this print statement f-string
nl = "\n" 


print(f"{nl}{nl}Election Results{nl}-------------------------------")
print(f"Total Votes: {total_votes}{nl}-------------------------------")
print(f"Kahn: {khan_pct}% ({khan_vote_total})")
print(f"Correy: {correy_pct}% ({correy_vote_total})")
print(f"Li: {li_pct}% ({li_vote_total})")
print(f"O'Tooley: {otooley_pct}% ({otooley_vote_total}){nl}-------------------------------")
print(f"Winner: {winner}{nl}-------------------------------")
print(f"{nl}{nl}")

# results_file = os.path.join('analysis', 'analysis.txt')
# with open(results_file, 'a') as analysis_write:
#     analysis_write.write(f"{nl}{nl}Election Results{nl}-------------------------------{nl}")
#     analysis_write.write(f"Total Votes: {total_votes}{nl}-------------------------------{nl}")
#     analysis_write.write(f"Kahn: {khan_pct}% ({khan_vote_total}){nl}")
#     analysis_write.write(f"Correy: {correy_pct}% ({correy_vote_total}){nl}")
#     analysis_write.write(f"Li: {li_pct}% ({li_vote_total}){nl}")
#     analysis_write.write(f"O'Tooley: {otooley_pct}% ({otooley_vote_total}){nl}-------------------------------{nl}")
#     analysis_write.write(f"Winner: {winner}{nl}-------------------------------{nl}")
#     analysis_write.write(f"{nl}{nl}")
