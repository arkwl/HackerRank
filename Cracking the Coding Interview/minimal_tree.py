def binary_search(array):
    midpoint = len(array)/2
    print(array)
    if(len(array) == 1):
        print(array[0])
        return
    else:
        print(array[midpoint])
        binary_search(array[0:midpoint])
        binary_search(array[midpoint+1:len(array)])

binary_search([1, 2, 3, 4, 6 ,7, 8])
