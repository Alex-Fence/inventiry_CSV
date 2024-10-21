import csv
from os import device_encoding

hw_dict = {}
with open('ZAMFIN.csv', 'r', newline = '', encoding = 'utf-8') as csv_file:
    csv_r = csv.reader(csv_file, delimiter='\t')
    for s in csv_r:
        if len(s) == 1:
            name_s = s[0]
            hw_dict[name_s] = []
        else:
            for i in s:
                if len(i) > 0:
                    hw_dict[name_s].append(i)
#print(hw_dict.keys())
hw_dict['Материнская плата'] = hw_dict.pop('\ufeffМатеринская плата')
for k,v in hw_dict.items():
    print(f'{k}: {v}')
# for device in hw_dict:
#     print(device)
dev_dict_cut = {}
print()
for device, options in hw_dict.items():
    match device:
        case 'Материнская плата':
            dev_dict_cut[device] = [options[0]]
        case 'Процессоры':
            dev_dict_cut[device] = [options[0]]
        case 'Оперативная память':
            dev_dict_cut[device] = [i for i in options if 'Объем' in i or 'Частота' in i]
        case 'Запоминающие устройства': pass
        case 'Видеоадаптеры': pass
        case 'Звуковые платы': pass
        case 'Адаптеры сетевого интерфейса': pass
        case 'Мониторы': pass
print(dev_dict_cut)