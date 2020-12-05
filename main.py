import os
import sys
from Insertion import *
from parse import *

if __name__=='__main__':
    cities = parse('/Users/lucas/worldcitiespop.csv')
    print(cities)
    
    