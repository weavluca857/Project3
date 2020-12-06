import sys
import os

def insertion_sort_latitude(list):
    for i in range(0, len(list)):
        key = list[i]
        j = i - 1
        while key.latitude < list[j].latitude and j >= 0:
            list[j+1] = list[j]
            j = j - 1
        
        list[j+1] = key


def insertion_sort_longitude(list):
    for i in range(0, len(list)):
        key = list[i]
        j = i - 1
        while key.latitude < list[j].latitude and j >= 0:
            list[j+1] = list[j]
            j = j - 1
        
        list[j+1] = key