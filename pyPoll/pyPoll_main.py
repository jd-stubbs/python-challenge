"""
Author: Justin Stubbs
@GitHub: jd-stubbs
GW Data Analytics Boot Camp
HW#3 Part 2 - Voting Analysis
"""

#import necessary libraries
import csv

#instantiate variables
total_votes = 0
candidates = []
votes = []

#set file path to election_data.csv
file = '../../Resources/election_data.csv'

#Open and read data from csv
with open(file, 'r') as data:
    x = csv.reader(data, delimiter=",")
    next(x)
    for i in x:
        #increment total vote count for each row in data
        total_votes += 1
        #if the candidate in the current row has not been encountered yet,
        #add their name to the candidates list and give them 1 vote in votes
        if i[2] not in candidates:
            candidates.append(i[2])
            votes.append(1)
        #otherwise, increment the vote count for the right candidate
        else:
            votes[candidates.index(i[2])] += 1

#calculate the percent of the total votes each candidate received
percent = [round((x / total_votes) * 100, 3) for x in votes]

#combine the candidates, their percent of the votes, and vote count
#sort the results, most votes to least
results = sorted(zip(candidates, percent, votes), key=lambda x: x[2], reverse=True)

#format report
sep = "-------------------------"
analysis = []
analysis.append("Election Results")
analysis.append(sep)
analysis.append("Total Votes: " + str(total_votes))
analysis.append(sep)
for i in range(len(results)):
    analysis.append(results[i][0] + ": " + str(results[i][1]) + "% (" + str(results[i][2]) + ")")
analysis.append(sep)
analysis.append("Winner: " + results[0][0])
analysis.append(sep)

#generate report
output_file = 'voting_analysis.txt'
with open(output_file, 'w') as report:
    for i in analysis:
        print(i)
        report.write(i + "\n")