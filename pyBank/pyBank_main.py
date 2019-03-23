"""
Author: Justin Stubbs
GW Data Analytics Boot Camp
HW#3 Part 1 - Budget Analysis
"""

#import necessary libraries
import csv

#instantiate variables
date = []
profit = []
net_total = 0
months = 0
change = []
sum_change = 0
increase = 0
decrease = 0
average_change = 0

#set file path to budget_data.csv
file = 'budget_data.csv'

#Open, read, and store data from csv
with open(file, 'r') as data:
    x = csv.reader(data, delimiter=",")
    next(x)
    for i in x:
        date.append(i[0])
        profit.append(i[1])

#count number of months
months = len(date)

#sum net profits
for i in range(len(profit)):
    net_total += int(profit[i])

#calculate and append change each month
#determine if current change is greater/less than max increase/decrease
#sum change for average calculation
for i in range(len(profit) - 1):
    change.append(int(profit[i+1]) - int(profit[i]))
    
    if change[i] > increase:
        increase = change[i]
    
    if change[i] < decrease:
        decrease = change[i]
    
    sum_change += change[i]

#calculate average monthly change
average_change = round(sum_change / len(change), 2)

analysis = []
analysis.append("Financial Analysis")
analysis.append("-----------------------------")
analysis.append("Total Months: " + str(months))
analysis.append("Total: $" + str(net_total))
analysis.append("Average Change: $" + str(average_change))
analysis.append("Greatest Increase in Profits: " + str(date[change.index(increase) + 1]) + " ($" + str(increase) + ")")
analysis.append("Greatest Decrease in Profits: " + str(date[change.index(decrease) + 1]) + " ($" + str(decrease) + ")")

output_file = 'financial_analysis.txt'
with open(output_file, 'w') as report:
    for i in analysis:
        print(i)
        report.write(i + "\n")