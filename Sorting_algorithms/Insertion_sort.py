#Insertion sort
#In insertion sort we first select the first element and find it's correct position and add it their

def insertion_sort(customList):
    for i in range(1, len(customList)): #first element is always sorted
        Key = customList[i] #This temp variable stores the current element
        j = i - 1
        while j >= 0 and Key < customList[i]:
            customList[j+1] = customList[j]
            j -= 1
        customList[j+1] = Key

    return customList

C_list = [3,2,4,5,2,4,35,2]
print(insertion_sort(C_list))

#This will take o(n) time complexity
#and O(1) space complexity
