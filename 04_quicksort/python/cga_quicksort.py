'''
TODO Write unit tests to compare this QS algo to the non-randomized one in the stock code
'''

import random

class CGAQS():

    def quicksort(self, inputList):
        lesser = []
        greater = []
        
        # first define the base case
        if len(inputList) < 2:
            return inputList
        # define the recursive case
        else:
            # find the pivot
            pivot = random.randrange(0, len(inputList))
            for i in range(len(inputList)):
                if i == pivot: # skip the pivot so we don't keep growing the list
                    continue
                if inputList[i] <= inputList[pivot]:
                    lesser.append(inputList[i])
                    # move that element into less than group
                else:
                    #move element into greater than group
                    greater.append(inputList[i])
            
            return self.quicksort(lesser) + [inputList[pivot]] + self.quicksort(greater)

if __name__ == '__main__':
    qs = CGAQS()
    random.seed()
    inputList = [54, 8, 73, 1, 23, 54, 12, 1, 53, 78, 76, 765, 2354, 223, 8, 44, 53458, 2, 3, 55]
    # inputList = [8, 2, 23, 14, 1]
    print(qs.quicksort(inputList))
