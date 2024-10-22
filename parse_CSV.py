import csv
from os import device_encoding

def
hw_dict = {}
# загрузка CSV файла
with open('ZAMFIN.csv', 'r', newline='', encoding='utf-8') as csv_file:
    csv_r = csv.reader(csv_file, delimiter='\t')
    # формирование словаря
    for s in csv_r:
        if len(s) == 1:
            name_s = s[0]
            hw_dict[name_s] = []
        else:
            # отсеивание пустых значений
            for i in s:
                if len(i) > 0:
                    hw_dict[name_s].append(i)
# переделка ключа Материнская плата из-за его искажения при загрузки
hw_dict['Материнская плата'] = hw_dict.pop('\ufeffМатеринская плата')
# печать полученного словаря
# for k, v in hw_dict.items():
#     print(f'{k}: {v}')

dev_dict_cut = {}
print()
# очистка словаря от лишних значений
for device, options in hw_dict.items():
    match device:
        case 'Материнская плата':
            dev_dict_cut[device] = [options[0]]
        case 'Процессоры':
            dev_dict_cut[device] = [options[0]]
        case 'Оперативная память':
            dev_dict_cut[device] = [i for i in options if 'Объем' in i or 'Частота' in i]
        case 'Запоминающие устройства':
            dev_dict_cut[device] = [i for i in options if not ('Описание' in i or 'Поставщик' in i)]
        case 'Видеоадаптеры':
            if len(options) > 5:
                dev_dict_cut[device] = [options[0], options[5]]
            else:
                dev_dict_cut[device] = [options[0]]
        case 'Звуковые платы':
            dev_dict_cut[device] = [options[0]]
        case 'Адаптеры сетевого интерфейса':
            dev_dict_cut[device] = [options[0]]
        case 'Мониторы':
            dev_dict_cut[device] = [options[1]]

for device, options in dev_dict_cut.items():
    print(f'{device}: {options}')
