27#in this we have to search the particular element in 2d array

import numpy as np

arr1 = np.array([[1,2,3,4],[2,33,1,4],[1,2,3,4]])
print(arr1)



#in this we will perform the linear search

def linear_search(array, target):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == target:
                return "The value is located at index "+str(i)+" "+str(j)
    return "Element not found"

print(linear_search(arr1, 33))

#the time complexity will be quadratic
#the space complexity will be o(1)


