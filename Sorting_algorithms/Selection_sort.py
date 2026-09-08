 #Selection sort

"""
The smallest element is selected from the unsorted array and swapped with the left_most element (1st), and that element
becomes the part of the sorted array.
This process continues moving unsorted array boundaries by one element to the right.

"""


def selection_sort(customList):
    for i in range(len(customList)):
        min_index = i
        for j in range(i+1, len(customList)):
            if customList[min_index] > customList[j]:
                min_index = j#index
        customList[i], customList[min_index] = customList[min_index], customList[i] #current index will be greater than the min_index value so we will swap them outside the loop


    print(customList)


C_list = [1,1,0,2,1,0]
selection_sort(C_list)

#Time_complexity => o(n^2)
#Space_complexity => o(n)

#USAGE -> When we have insufficient memory
#Easy to implement




