import sys
import os

def insertion_sort(list):
    for i in range(0, len(list)):
        j = i
        while list[j] < list[j-1] and j-1 >= 0:
            temp = list[j]
            list[j] = list[j-1]
            list[j-1] = temp
            j = j -1
