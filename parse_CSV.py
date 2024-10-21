import csv

with open('zamfin.csv', 'r', newline = '', encoding = 'utf-8') as csv_file:
    csv_r = csv.reader(csv_file, delimiter='\t')
    for s in csv_r:
        print(s)
