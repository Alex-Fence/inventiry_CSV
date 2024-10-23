import csv
import os
from os import listdir


def get_data_from_file(f_name: str) -> dict:
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
                dev_dict_cut[device] = [i for i in options if not ('Описание' in i or 'Поставщик' in i)]
                # dev_dict_cut[device] = []
                # for d in range(0, len(options), 6):
                #     dev_dict_cut[device].append([i for i in options[d:d + 6] if not ('Описание' in i or 'Поставщик' in i)])
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
def write_data_to_file(data: dict, f_name: str):
    os.chdir('..')
    with open(f_name, 'a', newline='', encoding='utf-8') as csv_file:
        csv_w = csv.writer(csv_file)

        # Записываем данные построчно
        for key, values in data.items():
            if isinstance(values[0], list):  # Если значения - это списки
                for item in values:
                    csv_file.write(f'{key},"{", ".join(item)}"\n')
            else:
                csv_file.write(f'{key},"{values[0]}"\n')


os.chdir('./pc_dir')
comp_data = get_data_from_file('ZAMFIN.csv')
write_data_to_file(comp_data, 'comp_data.csv')
for device, options in comp_data.items():
    print(f'{device}: {options}')
# for comp in listdir():
#     print(comp[:-4])
#     comp_data = get_data_from_file(comp)
#     for device, options in comp_data.items():
#         print(f'{device}: {options}')


