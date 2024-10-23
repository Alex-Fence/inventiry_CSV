import csv
import os
from os import listdir


def get_data_from_file(f_name: str) -> dict:
    os.chdir('./pc_dir')
    hw_dict = {}
    # загрузка CSV файла
    with open(f_name, 'r', newline='', encoding='utf-8') as csv_file:
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
    #     print(f'{k}: {len(v)}')

    dev_dict_cut = {}
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
                #dev_dict_cut[device] = [i for i in options if not ('Описание' in i or 'Поставщик' in i)]
                dev_dict_cut[device] = []
                for d in range(0, len(options), 6):
                    dev_dict_cut[device].append([i for i in options[d:d + 6] if not ('Описание' in i or 'Поставщик' in i)])
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
    return dev_dict_cut

#Запись в файл csv
def write_data_to_file(comp_name: str, data: dict):
    os.chdir('..')
    with open('comp_data.csv', 'a', newline='', encoding='utf-8') as csv_file:
        csv_file.write('\n')
        csv_file.write(comp_name[:-4] + '\n')

        # Записываем данные построчно
        for key, values in data.items():
            if len(values) > 0:
                if isinstance(values[0], list):
                    for v in values:
                        csv_file.write(f"{key},{', '.join(v)}\n")
                else:
                    csv_file.write(f"{key},{', '.join(values)}\n")



# os.chdir('./pc_dir')
# comp_name = 'ZAMFIN.csv'
# comp_data = get_data_from_file(comp_name)
# write_data_to_file(comp_name, comp_data,)
# for device, options in comp_data.items():
#     print(f'{device}: {options}')
for comp in listdir('./pc_dir'):
    print(comp)
    comp_data = get_data_from_file(comp)
    # for device, options in comp_data.items():
    #     print(f'{device}: {options}')
    write_data_to_file(comp, comp_data)

