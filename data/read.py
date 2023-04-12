from pprint import pprint
import csv


with open("data/phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
  a = contacts_list[0]
  # v = str([i for i in a])
  # print(v)

with open("data/phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.DictReader(f, delimiter=",")
  contacts_list = list(rows)
  for i in contacts_list:
    # print(i)
    for v in i.items():
      print(v)

  # b = sorted(rows, key=lambda x: x['lastname', 'firstname'])
  # pprint(b)
# print(a[0:])
# for i in a:

#   print(i)