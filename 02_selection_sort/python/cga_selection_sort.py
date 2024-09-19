"""
TODO Learn how to implement a class here similar to the binary search solution.
Tricker because the selection_sort method will call find_min_val?
TODO Write my own unit test program to evaluate performance
TODO Write a recursive version of each of these programs
"""

# class SelectionSort():

def find_min_val(list) -> int:
    tempMin = list[0]
    index = 0
    minIndex = 0

    #iterate through our initial array looking for the max value
    for value in list:
        if value < tempMin:
            # each time we find a value greater than the current max, update the index
            minIndex = index  
            tempMin = value
        index += 1
    # return the index of the max value
    return minIndex

def selection_sort(list):
    # init sorted array at correct length to avoid moving array as it grows
    arrSorted = [None] * len(list) 
    # a = numpy.empty(n, dtype=object) # a more optimal implementation if we know the sorted array size?

    for i in range(len(list)):
        smallest = find_min_val(list)
        arrSorted[i] = list[smallest]
        list.pop(smallest) # modifying an input to this function seems like questionable practice.

    return arrSorted
    
if __name__ == '__main__':
    # ss = SelectionSort
    testList = [108, 15, -2, -51, -2]
    print('Unsorted list: ', testList)
    print('Sorted list: ', selection_sort(testList))