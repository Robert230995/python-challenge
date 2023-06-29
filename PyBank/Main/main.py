import os
import csv

'''
#csvpath = os.path.join('Resources', 'budget_data.csv')
csvpath ='../Resources/budget_data.csv'

with open(csvpath,encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

#Method 1: Plain Reading of CSV files
 with open(csvpath, encoding='UTF-8') as file_handler:
    lines = file_handler.read()
    print(lines)
    print(type(lines))
'''
csv_file_path = "../Resources/budget_data.csv"

def calculate_total_months(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        # Skip the header row
        next(reader)
        # Count the number of rows (months)
        total_months = sum(1 for row in reader)
    return total_months

# Example usage

total_months = calculate_total_months(csv_file_path)
print(f'Total number of months: {total_months}')

total_profit_loss = 0
        # Iterate over each row and sum the profit/loss values
        for row in reader:
            profit_loss = int(row[1])
            total_profit_loss += profit_loss
    return total_profit_loss




