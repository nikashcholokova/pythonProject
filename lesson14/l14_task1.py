import csv


class myClass:
    def __init__(self, var1, var2, var3, var4, var5, var6, var7, var8, var9, var10, var11, var12):
        self.ident = var1
        self.type = var2
        self.name = var3
        self.elevation_ft = var4
        self.continent = var5
        self.iso_country = var6
        self.iso_region = var7
        self.municipality = var8
        self.gps_code = var9
        self.iata_code = var10
        self.local_code = var11
        self.coordinates = var12


my_list = []


def search(search_attr: str, keyword: str, list_for_search: list):
    answ_list = []
    for i in list_for_search:
        if i.__getattribute__(search_attr) == keyword:
            answ_list.append(list_for_search[list_for_search.index(i)])

    if answ_list.__len__() == 0:
        return 'there is no match by field ' + search_attr + " and keyword " + keyword
    return answ_list


with open('airport-codes_csv.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        my_list.append(myClass(row[0], row[1], row[2], row[3], row[4], row[5], row[6],
                               row[7], row[8], row[9], row[10], row[11]))

print(search('iso_country', 'US', my_list))
# print(search('iata_code', '-', my_list))
# print(search('name', '-', my_list))
