

def insertion_sort_latitude(l):
    for i in range(0, len(l)):
        key = l[i]
        j = i - 1
        while key.lat < l[j].lat and j >= 0:
            l[j+1] = l[j]
            j = j - 1
        
        l[j+1] = key
        print(i)


def insertion_sort_longitude(l):
    for i in range(0, len(l)):
        key = l[i]
        j = i - 1
        while key.lon < l[j].lon and j >= 0:
            l[j+1] = l[j]
            j = j - 1
        
        l[j+1] = key

def shell_sort_latitude(l):

    size = len(l)
    print(size)
    gap = int(size/2)
    print(gap)
    while gap > 0:

        for i in range(gap, size):
            temp = l[i]

            j = i
            while j >= gap and l[j-gap].lat > temp.lat:
                l[j] = l[j-gap]
                j -= gap

            l[j] = temp
        gap = int(gap / 2)
        print(gap)

def shell_sort_longitude(l):

    size = len(l)
    gap = int(size/2)

    while gap > 0:

        for i in range(gap, size):
            temp = l[i]

            j = i
            while j >= gap and l[j-gap].lon > temp.lon:
                l[j] = l[j-gap]
                j -= gap

            l[j] = temp
        gap = int(gap / 2)
