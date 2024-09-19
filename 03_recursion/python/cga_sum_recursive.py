'''
TODO learn why my pop based method in line 10 didn't work
TODO implement a class
'''


def sum_recursive(list):
    if len(list) == 1:
        return list[0]
    else:
        # return list[0] + sum_recursive(list.pop(0))
        return list[0] + sum_recursive(list[1:])
    
if __name__ == '__main__':
    arr = [3, 15, 2, 6, 9, 23, 1, 11]
    print('The recucrsive sum is: ', sum_recursive(arr))
    print('The standard lib sum is', sum(arr))