

def insertion_sort_latitude(l):
    for i in range(0, len(l)):
        key = l[i]
        j = i - 1
        while key.latitude < l[j].latitude and j >= 0:
            l[j+1] = l[j]
            j = j - 1
        
        l[j+1] = key


def insertion_sort_longitude(l):
    for i in range(0, len(l)):
        key = l[i]
        j = i - 1
        while key.latitude < l[j].latitude and j >= 0:
            l[j+1] = l[j]
            j = j - 1
        
        l[j+1] = key

def shell_sort_latitude(l):

    size = len(l)
    gap = size/2

    while gap > 0:

        for i in range(gap, size):
            temp = l[i]

            j = i
            while j >= gap and l[j-gap].latitude > temp.latitude:
                l[j] = l[j-gap]
                j -= gap

            l[j] = temp
        gap = gap / 2

def shell_sort_longitude(l):

    size = len(l)
    gap = size/2

    while gap > 0:

        for i in range(gap, size):
            temp = l[i]

            j = i
            while j >= gap and l[j-gap].longitude > temp.longitude:
                l[j] = l[j-gap]
                j -= gap

            l[j] = temp
        gap = gap / 2
