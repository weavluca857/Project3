import csv
from city import City

def parse(file, size = 500000):
    cities = []
    with open(file, 'r') as f:
        csv_reader = csv.reader(f)
        l = 0
        for row in csv_reader:
            if l =! 0 and l < size:
                cities.append(City(row[6], row[5], row[1]))
                l = l + 1
    return cities
            