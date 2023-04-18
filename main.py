import csv
import re

def read(file):
   with open(file, encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    return  contacts_list

def number_update(contacts_list):
    pattern = r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)' \
                            r'(\-*)(\d{3})(\s*)(\-*)(\d{2})(\s*)(\-*)' \
                            r'(\d{2})(\s*)(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)'
    pattern_bloc = r'+7(\4)\8-\11-\14\15\17\18\19\20'
    contacts_list_new = list()
    for value in contacts_list:
        values = ','.join(value)
        new_values = re.sub(pattern, pattern_bloc, values)
        list_new = new_values.split(',')
        contacts_list_new.append(list_new)
    return contacts_list_new

def name_change(contacts_list):
    pattern = r'^([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)' \
                       r'(\s*)(\,?)([А-ЯЁа-яё]*)(\,?)(\,?)(\,?)'
    pattern_bloc = r'\1\3\10\4\6\9\7\8'
    contacts_list_new = list()
    for value in contacts_list:
        values = ','.join(value)
        new_values = re.sub(pattern, pattern_bloc, values)
        list_new = new_values.split(',')
        contacts_list_new.append(list_new)
    return contacts_list_new

def list_change(contacts_list):
    for i in contacts_list:
        for j in contacts_list:
            if i[0] == j[0] and i[1] == j[1] and i != j:
                if i[2] == (' '):
                    i[2] = j[2]
                if i[3] == (' '):
                    i[3] = j[3]
                if i[4] == (' '):
                    i[4] = j[4]
                if i[5] == (' '):
                    i[5] = j[5]
                if i[6] == (' '):
                    i[6] = j[6]
    contacts_list_new = list()
    for value in contacts_list:
        if value not in contacts_list_new:
            contacts_list_new.append(value)
    return contacts_list_new

def write_file(contacts_list):
    with open("data/phonebook.csv", "w", encoding='utf-8') as f:
        data_writer = csv.writer(f, delimiter=',')
        data_writer.writerows(contacts_list)


if __name__ == '__main__':
    file = read("data/phonebook_raw.csv")
    file = number_update(file)
    file = name_change(file)
    file = list_change(file)
    write_file(file)
    print(file)