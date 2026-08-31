#In bubble sort we first compare each adjacent pairs of element and swap them if the next element is smaller than the current element

def bubble_sort(customList):
    for i in range(len(customList)-1):#The final condition will always be true
        for j in range(len(customList)-i-1):#The final 4 will always satisfy the condition
            if customList[j] > customList[j+1]:
                customList[j], customList[j+1] = customList[j+1], customList[j]

    print(customList)

cList = [2,1,6,32,562,14,3]
bubble_sort(cList)

#Time-Complexity = o(n^2)
#Space-Complexity = o(1)

