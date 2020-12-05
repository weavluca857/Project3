import os
import sys
import csv

def parse(file):
    line = {}
    with open(file, 'r') as f:
        csv_reader = csv.reader(f, delimeter=',')
        l = 0
        if l == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1