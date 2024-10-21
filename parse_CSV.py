import csv

with open('zamfin.csv', 'r', encoding='utf-8') as csv_file:
    csv_r = csv.reader(csv_file)
for s in csv_r:
    print(s)
