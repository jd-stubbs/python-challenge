"""
Author: Justin Stubbs
GW Data Analytics Boot Camp
HW#3 Part 1 - Budget Analysis
"""

#import necessary libraries
import csv

#instantiate variables
net_total = 0
months = 0
prev = 0
sum_change = 0
inc = {"date": "", "profit": 0}
dec = {"date": "", "profit": 0}
avg_change = 0

#set file path to budget_data.csv
file = '../../Resources/budget_data.csv'

#Open, read, and process data from csv
with open(file, 'r') as data:
    x = csv.reader(data, delimiter=",")
    
    #ignore header
    next(x)
    
    #process first row to set key variables
    i = next(x)
    months += 1
    net_total += int(i[1])
    prev = int(i[1])
    
    #finish processing file starting with the 3rd line (2nd data line)
    for i in x:
        #count months
        months += 1
        
        #sum total profits
        net_total += int(i[1])
        
        #calculate monthly change in profits
        change = prev - int(i[1])
        
        #sum total change in profits for average calculation
        sum_change += change
        
        #compare change to previous high and replace if higher
        if change > inc['profit']:
            inc['profit'] = change
            inc['date'] = i[0]
        
        #compare change to previous low and replace if lower
        if change < dec['profit']:
            dec['profit'] = change
            dec['date'] = i[0]
        
        #set current profit as next 'previous' profit
        prev = int(i[1])


#calculate average monthly change
avg_change = round(sum_change / (months - 1), 2)

#format report
analysis = []
analysis.append("Financial Analysis")
analysis.append("-----------------------------")
analysis.append("Total Months: " + str(months))
analysis.append("Total: $" + str(net_total))
analysis.append("Average Change: $" + str(avg_change))
analysis.append("Greatest Increase in Profits: " + inc['date'] + " ($" + str(inc['profit']) + ")")
analysis.append("Greatest Decrease in Profits: " + dec['date'] + " ($" + str(dec['profit']) + ")")

#generate report
output_file = 'financial_analysis.txt'
with open(output_file, 'w') as report:
    for i in analysis:
        print(i)
        report.write(i + "\n")