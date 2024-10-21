import csv
hw_dict = {}
with open('zamfin.csv', 'r', newline = '', encoding = 'utf-8') as csv_file:
    csv_r = csv.reader(csv_file, delimiter='\t')
    for s in csv_r:
        if len(s) == 1:
            name_s = s[0]
            hw_dict[name_s] = []
        else:
            for i in s:
                if len(i) > 0:
                    hw_dict[name_s].append(i)
for k,v in hw_dict.items():
    print(f'{k}: {v}')
