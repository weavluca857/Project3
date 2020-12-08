import csv
from city import City

def parse(file, n):
    cities = []
    with open(file, 'r') as f:
        csv_reader = csv.reader(f)
        l = 0
        for row in csv_reader:
            if l != 0 and l < n:
                cities.append(City(row[6], row[5], row[1]))
                l = l + 1
            elif l == 0:
                l = l + 1
            else:
                return cities