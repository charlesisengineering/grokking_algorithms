'''
TODO Understand why we have to pass self to search_iterative
TODO Compare my recursive solution to the official one
TODO Read about classes and methods in python
TODO check out unit testing script
'''


class BinarySearch():

    # define a method for doing iterative binary search
    def search_iterative(self, list, target):
      low = 0
      high = len(list) -1
      
      # once we have one element remaining, low = high
      while low <= high:
         # with binary search we always guess the middle element
         middle = (low + high)//2 # use // for floor division (integer division)

         guess = list[middle] # take a guess at our middle positon

         if guess == target:
            return middle # return the position if we've found target
         elif guess < target:
            low = middle + 1 # if our guess was too low let's search the region above
         else:
            high = middle -1

      return None # this should be called if our loop converages (one element left) but we haven't found a match

          
    # define a method for doing recursive binary search
    def search_recursive(self, list, low, high, target):
       
       middle = (low + high)//2
       guess = list[middle]

       if guess == target:
          return middle
       else:
          while low < high:
            if guess < target:
               low = middle + 1
            else:
               high = middle - 1
            # needs return in order to give the right value when we call from unit test
            # can't include self in the call when we use in the unit test implementation
            return self.search_recursive(list, low, high, target) 
       return None
    

if __name__ == "__main__": # only run the below if we're calling script directly, not if some other program calls it
  # We must initialize the class to use the methods of this class
  bs = BinarySearch()
  my_list = [1, 3, 5, 7, 9, 12, 15, 18, 21, 24, 27, 30]
  
  print("Iterative search result for target = 3: ", bs.search_iterative(my_list, 18))

  print("Iterative search result for target = -1: ", bs.search_iterative(my_list, -1))

  print("Recursive search result for target = 3: ", bs.search_iterative(my_list, 18))

  print("Recursive search result for target = -1: ", bs.search_iterative(my_list, -1))