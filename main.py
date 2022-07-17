import csv
from Employee import *
from prettytable import PrettyTable

if __name__ == '__main__':
    emp = []
    x = PrettyTable()
    with open("content.csv", 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        x.field_names = header
        for row in csvreader:
            emp.append(employee(int(row[0]), row[1], int(row[2]), row[3], row[4], row[5], int(row[6])))
            x.add_row(row)
    print(x)
