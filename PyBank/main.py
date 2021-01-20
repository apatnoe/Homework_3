
# name dependencies
import os
import csv

# create file path

input_path = "Resources/budget_data.csv"

# variables for month count and lists

month_count = 0
month_list = []
profit_list = []
monthly_change = []

# function to create a list of monthly profit/losses

def finances(monthly_data):

    # name variables for both columns
    month = str(monthly_data[0])
    profit_loss = int(monthly_data[1])

    # write values to the list
    month_list.append(month)
    profit_list.append(profit_loss)

# read input file
with open(input_path, "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    header = next(csv_reader)
 
    # loop through each row
    for row in csv_reader:

        # add a month to month count
        month_count = month_count + 1

        # loop through the function to write each month to the list
        finances(row)

# once the list is complete, determine the length of the profit list
length = len(profit_list)

# loop through the list, starting at 1 to avoid the first month comparing to the last month of the set
for i in range(1,length):

    #create a new list that will take the change between the two months
    monthly_change.append(profit_list[i]-profit_list[i-1])

# create output variables
net_pl = sum(profit_list)
average_change = sum(monthly_change)/len(monthly_change)
greatest_increase = max(monthly_change)
greatest_decrease = min(monthly_change)

# create variables for the index of the least/greatest months
greatest_increase_index = monthly_change.index(max(monthly_change))
greatest_decrease_index = monthly_change.index(min(monthly_change))

# use those index values to get the months
greatest_increase_month = month_list[greatest_increase_index+1]
greatest_decrease_month = month_list[greatest_decrease_index+1]

#display output in terminal 
print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {month_count}')
print(f'Total: ${net_pl}')
print(f'Average Change: ${average_change:.2f}')
print(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')

# write output to a text file - each on a new line
text_file = open("Analysis/Output.txt", "w")
text_file.write("Financial Analysis")
text_file.write("\n")
text_file.write("----------------------------")
text_file.write("\n")
text_file.write(f'Total Months: {month_count}')
text_file.write("\n")
text_file.write(f'Total: ${net_pl}')
text_file.write("\n")
text_file.write(f'Average Change: ${average_change:.2f}')
text_file.write("\n")
text_file.write(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})')
text_file.write("\n")
text_file.write(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')





